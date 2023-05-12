import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pydicom
from skimage.morphology import binary_dilation, binary_erosion


def mean_absolute_error(img_input: np.ndarray, img_reference) -> np.ndarray:
    """ Compute the MAE between two images. """
    # Your code here:
    #   ...
    return np.mean(np.abs(img_input - img_reference))


def mean_squared_error(img_input: np.ndarray, img_reference) -> np.ndarray:
    """ Compute the MAE between two images. """
    # Your code here:
    #   ...
    return np.mean((img_input - img_reference)**2)


def mutual_information(img_input: np.ndarray, img_reference) -> np.ndarray:
    """ Compute the Shannon Mutual Information between two images. """
    # Your code here:
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
