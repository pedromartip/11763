import logging

import numpy as np
import matplotlib.pyplot as plt
import pydicom

log = logging.getLogger(__name__)


def get_amygdala_mask(img_atlas):
    log.info('Task 1.1: Find binary mask of amygdala')
    # YOUR CODE HERE
    # ...
    # ...
    amygdala_mask = np.empty(shape=(100, 100, 100))
    # ...

    # Plot mask
    plt.imshow(np.max(amygdala_mask, axis=0))
    # Return
    return amygdala_mask


def visualize_region(img_phantom, region_mask):
    log.info('Task 2.1: Find centroid of mask')
    # YOUR CODE HERE
    # ...
    # ...
    centroid = (50, 50, 50)
    # ...

    log.info('Task 2.2: Plot slices of dcm_image centered with respect to mask')
    # YOUR CODE HERE
    # ...
    # ...
    coronal = img_phantom[:, :, centroid[2]]
    # sagital = img_phantom[:, :, centroid[2]]
    # axial = img_phantom[:, :, centroid[2]]
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].imshow(coronal)
    # ...


def find_region_volume(region_mask):
    log.info('Task 3.1: Find volume of given region')
    # YOUR CODE HERE
    # ...
    # ...
    region_volume = 0
    # ...

    log.info('Task 3.2: Find surface of given region')
    # YOUR CODE HERE
    # ...
    # ...
    region_surface = 0
    # ...

    # Show info
    return region_volume, region_surface


if __name__ == '__main__':
    # Load data
    dcm_phantom = pydicom.dcmread('data/icbm_avg_152_t1_tal_nlin_symmetric_VI_alternative.dcm')
    img_phantom = dcm_phantom.pixel_array[6:-6, 6:-6, 6:-6]
    dcm_atlas = pydicom.dcmread('data/AAL3_1mm.dcm')
    img_atlas = dcm_atlas.pixel_array

    amygdala_mask = get_amygdala_mask(img_atlas)
    visualize_region(img_phantom, amygdala_mask)
    vol, surf = find_region_volume(amygdala_mask)

    log.info('Amygdala volume: {} mm^3'.format(vol))
    log.info('Amygdala surface: {} mm^2'.format(surf))
