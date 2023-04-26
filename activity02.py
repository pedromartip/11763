import matplotlib
import pydicom
import numpy as np
from matplotlib import pyplot as plt
from skimage import measure

from utils import filepath


def median_sagittal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the median sagittal plane of the CT image provided. """
    _, _, sz_z = img_dcm.shape
    sagittal_plane = img_dcm[:, :, sz_z//2]             # Why //2? Why on third dimension?
    sagittal_plane = np.rot90(sagittal_plane, k=-1)     # Better visualization
    return sagittal_plane


def segment_bones(img_ct: np.ndarray) -> np.ndarray:
    """ Segment the bones of a CT image. """
    # Your code here:
    #   should return a boolean mask (positive/negative) or an integer mask (labels)?
    #   See `skimage.measure.label(...)`.
    # ...
    mask_bone = img_ct > 250    # Which is the best threshold?
    mask_bone_labels = measure.label(mask_bone)
    return mask_bone_labels


def visualize_side_by_side(img: np.ndarray, mask: np.ndarray):
    """ Visualize image and mask in two different subplots. """
    # Your code here:
    #   See `plt.subplot(...)`, `plt.imshow(...)`, `plt.show(...)`.
    #   Which colormap should you choose?
    #   Which aspect ratio should you choose?
    # ...
    plt.subplot(211), plt.imshow(img, cmap=matplotlib.colormaps['bone'], aspect=0.98/3.27)
    plt.subplot(212), plt.imshow(mask, cmap=matplotlib.colormaps['prism'], aspect=0.98/3.27)
    plt.show()


def apply_cmap(img: np.ndarray, cmap_name: str = 'bone') -> np.ndarray:
    """ Apply a colormap to a 2D image. """
    # Your code here: See `matplotlib.colormaps[...]`.
    # ...
    cmap_function = matplotlib.colormaps[cmap_name]
    return cmap_function(img)


def visualize_alpha_fusion(img: np.ndarray, mask: np.ndarray, alpha: float = 0.25):
    """ Visualize both image and mask in the same plot. """
    # Your code here:
    #   Remember the Painter's Algorithm with alpha blending
    #   https://en.wikipedia.org/wiki/Alpha_compositing
    # ...
    img_sagittal_cmapped = apply_cmap(img, cmap_name='bone')    # Why 'bone'?
    mask_bone_cmapped = apply_cmap(mask, cmap_name='prism')     # Why 'prism'?
    mask_bone_cmapped = mask_bone_cmapped * mask[..., np.newaxis].astype('bool')

    alpha = 0.25
    plt.imshow(img_sagittal_cmapped * (1-alpha) + mask_bone_cmapped * alpha, aspect=0.98/3.27)
    plt.title(f'Segmentation with alpha {alpha}')
    plt.show()


if __name__ == '__main__':
    dcm_path = filepath('CT.dcm')
    dcm = pydicom.dcmread(dcm_path)   # Load DICOM file
    img_dcm = dcm.pixel_array         # Get pixel array
    print(dcm)                          # Print DICOM headers

    img_sagittal = median_sagittal_plane(img_dcm)
    mask_bone = segment_bones(img_sagittal)

    visualize_side_by_side(img_sagittal, mask_bone)
    visualize_alpha_fusion(img_sagittal, mask_bone)
