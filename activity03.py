import matplotlib
import pydicom
import numpy as np
import scipy
from matplotlib import pyplot as plt

from utils import filepath


def median_sagittal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the median sagittal plane of the CT image provided. """
    return img_dcm[:, img_dcm.shape[1]//2, :]    # Why //2?


def median_coronal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the median sagittal plane of the CT image provided. """
    return img_dcm[:, :, img_dcm.shape[2]//2]


def rotate_on_axial_plane(img_dcm: np.ndarray, angle) -> np.ndarray:
    """ Rotate the image on the axial plane. """
    # Your code here:
    #   See `scipy.ndimage.rotate(...)`
    # ...
    return scipy.ndimage.rotate(img_dcm, angle, axes=(0, 1), reshape=False)


if __name__ == '__main__':
    dcm_path = filepath('CT.dcm')
    dcm = pydicom.dcmread(dcm_path)     # Load DICOM file
    print(dcm)                          # Print DICOM headers
    pixel_len_mm = [3.27, 0.98, 0.98]   # Pixel length in mm [z, y, x]

    img_dcm = dcm.pixel_array           # Get pixel array
    img_dcm = np.flip(img_dcm, axis=0)  # Change orientation (better visualization)


    plt.subplot(1, 2, 1)
    plt.imshow(median_sagittal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[1])
    plt.subplot(1, 2, 2)
    plt.imshow(median_coronal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[2])
    plt.show()

