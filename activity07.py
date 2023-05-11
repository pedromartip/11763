import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pydicom
from skimage.morphology import binary_dilation, binary_erosion


def get_amygdala_mask(img_atlas: np.ndarray) -> np.ndarray:
    # Your code here:
    #   ...


def find_centroid(mask: np.ndarray) -> np.ndarray:
    # Your code here:
    #   Consider using `np.where` to find the indices of the voxels in the mask
    #   ...


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


def find_region_volume(region_mask):
    """ Returns the volume of the region in mm^3. """
    # Your code here:
    #   ...


def find_region_surface(mask):
    """ Returns the surface of the region in mm^2. """
    # Your code here:
    #   See `skimage.morphology.binary_erosion()` and `skimage.morphology.binary_dilation()`
    #   ...


if __name__ == '__main__':
    # Load data
    dcm_phantom = pydicom.dcmread('data/icbm_avg_152_t1_tal_nlin_symmetric_VI_alternative.dcm')
    img_phantom = dcm_phantom.pixel_array[6:-6, 6:-6, 6:-6]     # Crop phantom to atlas size
    dcm_atlas = pydicom.dcmread('data/AAL3_1mm.dcm')
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
