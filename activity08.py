import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pydicom
from skimage.morphology import binary_dilation, binary_erosion

from utils import filepath


def get_amygdala_mask(img_atlas: np.ndarray) -> np.ndarray:
    # Your code here:
    #   ...
    amygdala_mask = np.zeros_like(img_atlas)
    amygdala_mask[img_atlas == 45] = 1
    amygdala_mask[img_atlas == 46] = 1
    return amygdala_mask


def find_centroid(mask: np.ndarray) -> np.ndarray:
    # Your code here:
    #   Consider using `np.where` to find the indices of the voxels in the mask
    #   ...
    idcs = np.where(mask == 1)
    centroid = np.stack([
        np.mean(idcs[0]),
        np.mean(idcs[1]),
        np.mean(idcs[2]),
    ])
    return centroid


def visualize_axial_slice(
        img: np.ndarray,
        mask: np.ndarray,
        mask_centroid: np.ndarray,
        ):
    """ Visualize the axial slice (firs dim.) of a single region with alpha fusion. """
    # Your code here
    #   Remember `matplotlib.colormaps['cmap_name'](...)`
    #   See also `matplotlib.colors.Normalize(vmin=..., vmax=...)`
    #   ...
    img_slice = img[mask_centroid[0].astype('int'), :, :]
    mask_slice = mask[mask_centroid[0].astype('int'), :, :]

    cmap = matplotlib.colormaps['bone']
    norm = matplotlib.colors.Normalize(vmin=np.amin(img_slice), vmax=np.amax(img_slice))
    fused_slice = \
        0.5*cmap(norm(img_slice))[..., :3] + \
        0.5*np.stack([mask_slice, np.zeros_like(mask_slice), np.zeros_like(mask_slice)], axis=-1)
    plt.imshow(fused_slice)
    plt.show()


def find_region_volume(region_mask):
    """ Returns the volume of the region in mm^3. """
    # Your code here:
    #   ...
    return np.sum(region_mask)


def find_region_surface(mask):
    """ Returns the surface of the region in mm^2. """
    # Your code here:
    #   See `skimage.morphology.binary_erosion()` and `skimage.morphology.binary_dilation()`
    #   ...
    inner_surface = mask - binary_erosion(mask, np.ones((3, 3, 3)))
    outer_surface = binary_dilation(mask, np.ones((3, 3, 3))) - mask
    return (np.sum(inner_surface) + np.sum(outer_surface) ) / 2     # Average of inner and outer surface


if __name__ == '__main__':
    # Load data
    dcm_phantom = pydicom.dcmread(filepath('icbm_avg_152_t1_tal_nlin_symmetric_VI_alternative.dcm'))
    img_phantom = dcm_phantom.pixel_array[6:-6, 6:-6, 6:-6]     # Crop phantom to atlas size
    dcm_atlas = pydicom.dcmread(filepath('AAL3_1mm.dcm'))
    img_atlas = dcm_atlas.pixel_array

    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(img_phantom[100, :, :], cmap='bone')
    axs[1].imshow(img_atlas[100, :, :], cmap='tab20')
    fig.show()

    amygdala_mask = get_amygdala_mask(img_atlas)
    mask_centroid = find_centroid(amygdala_mask)
    visualize_axial_slice(img_phantom, amygdala_mask, mask_centroid)

    vol = find_region_volume(amygdala_mask)
    surf = find_region_surface(amygdala_mask)

    print('Amygdala volume:')
    print(f'  >> Result: {vol} mm^3')
    print(f'  >> Expected: 3744 mm^3')

    print('Amygdala surface:')
    print(f'  >> Result: {surf} mm^2')
    print(f'  >> Expected: 1849-6920 mm^2 (depending on the approximation)')
