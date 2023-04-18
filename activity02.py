import cv2
import pydicom
import numpy as np
from matplotlib import pyplot as plt
from skimage import measure


def load_dcm(filename):
    return pydicom.dcmread(f'data/{filename}')


def main():
    dcm = load_dcm(filename='16351644_s1_CT_PETCT.dcm')

    img_dcm = dcm.pixel_array
    img_sagital = np.rot90(img_dcm[:, :, 255], k=-1)
    img_sagital = img_sagital
    img_sagital_cmapped = plt.cm.get_cmap('bone')(img_sagital)

    mask_bone = img_sagital > 250
    mask_bone_labels = measure.label(mask_bone)
    mask_bone_segmentation = plt.cm.get_cmap('prism')(mask_bone_labels) * mask_bone[..., np.newaxis]

    [print(f'{k}: {v}') for k, v in dcm.items()]
    plt.subplot(211), plt.imshow(img_sagital, cmap=plt.cm.get_cmap('bone'), aspect=0.98/3.27)
    plt.subplot(212), plt.imshow(mask_bone_segmentation, aspect=0.98/3.27)
    plt.show()

    plt.subplot(211), plt.imshow(img_sagital, cmap=plt.cm.get_cmap('bone'), aspect=0.98/3.27)
    plt.subplot(212), plt.imshow(img_sagital_cmapped * 0.75 + mask_bone_segmentation * 0.25,
                                 aspect=0.98/3.27)
    plt.title('Segmentation with alpha 0.25')
    plt.show()


if __name__ == '__main__':
    main()
