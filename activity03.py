import os

import matplotlib
import pydicom
import numpy as np
import scipy
from matplotlib import pyplot as plt, animation

from utils import filepath


def median_sagittal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the median sagittal plane of the CT image provided. """
    return img_dcm[:, :, img_dcm.shape[1]//2]    # Why //2?


def median_coronal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the median sagittal plane of the CT image provided. """
    return img_dcm[:, img_dcm.shape[2]//2, :]


def MIP_sagittal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the maximum intensity projection on the sagittal orientation. """
    # Your code here:
    #   See `np.max(...)`
    # ...


def AIP_sagittal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the average intensity projection on the sagittal orientation. """
    # Your code here:
    #   See `np.mean(...)`
    # ...


def MIP_coronal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the maximum intensity projection on the coronal orientation. """
    # Your code here:
    # ...


def AIP_coronal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the average intensity projection on the coronal orientation. """
    # Your code here:
    # ...


def rotate_on_axial_plane(img_dcm: np.ndarray, angle_in_degrees: float) -> np.ndarray:
    """ Rotate the image on the axial plane. """
    # Your code here:
    #   See `scipy.ndimage.rotate(...)`
    # ...


if __name__ == '__main__':
    dcm_path = filepath('CT.dcm')
    dcm = pydicom.dcmread(dcm_path)     # Load DICOM file
    print(dcm)                          # Print DICOM headers
    pixel_len_mm = [3.27, 0.98, 0.98]   # Pixel length in mm [z, y, x]

    img_dcm = dcm.pixel_array           # Get pixel array
    img_dcm = np.flip(img_dcm, axis=0)  # Change orientation (better visualization)

    # Show median planes
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(median_sagittal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[1])
    ax[0].set_title('Sagittal')
    ax[1].imshow(median_coronal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[2])
    ax[1].set_title('Coronal')
    fig.suptitle('Median planes')
    plt.show()

    # Show MIP/AIP/Median planes
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(median_sagittal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[1])
    ax[0].set_title('Median')
    ax[1].imshow(MIP_sagittal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[1])
    ax[1].set_title('MIP')
    ax[2].imshow(AIP_sagittal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[1])
    ax[2].set_title('AIP')
    fig.suptitle('Sagittal')
    plt.show()
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(median_coronal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[1])
    ax[0].set_title('Median')
    ax[1].imshow(MIP_coronal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[1])
    ax[1].set_title('MIP')
    ax[2].imshow(AIP_coronal_plane(img_dcm), cmap=matplotlib.colormaps['bone'], aspect=pixel_len_mm[0]/pixel_len_mm[1])
    ax[2].set_title('AIP')
    fig.suptitle('Coronal')
    plt.show()

    # Create projections varying the angle of rotation
    #   Configure visualization colormap
    img_min = np.amin(img_dcm)
    img_max = np.amax(img_dcm)
    cm = matplotlib.colormaps['bone']
    fig, ax = plt.subplots()
    #   Configure directory to save results
    os.makedirs('results/MIP/', exist_ok=True)
    #   Create projections
    n = 6
    projections = []
    for idx, alpha in enumerate(np.linspace(0, 360*(n-1)/n, num=n)):
        rotated_img = rotate_on_axial_plane(img_dcm, alpha)
        projection = MIP_sagittal_plane(rotated_img)
        plt.imshow(projection, cmap=cm, vmin=img_min, vmax=img_max, aspect=pixel_len_mm[0] / pixel_len_mm[1])
        plt.savefig(f'results/MIP/Projection_{idx}.png')      # Save animation
        projections.append(projection)  # Save for later animation
    # Save and visualize animation
    animation_data = [
        [plt.imshow(img, animated=True, cmap=cm, vmin=img_min, vmax=img_max, aspect=pixel_len_mm[0] / pixel_len_mm[1])]
        for img in projections
    ]
    anim = animation.ArtistAnimation(fig, animation_data,
                              interval=250, blit=True)
    anim.save('results/MIP/Animation.gif')  # Save animation
    plt.show()                              # Show animation

