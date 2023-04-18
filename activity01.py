import cv2
import pydicom
import numpy as np
from matplotlib import pyplot as plt

from utils import filepath


def load_dcm(filepath: str):
    """ Load a DICOM file. """
    # YOUR CODE HERE
    # ...


def compute_snr(signal_power: float, noise_power: float):
    """ Compute the signal-to-noise ratio (SNR) of a signal. """
    # YOUR CODE HERE
    # ...


def compute_cnr(signal_contrast: float, noise_power: float):
    """ Compute the contrast-to-noise ratio (CNR) of a signal. """
    # YOUR CODE HERE
    # ...


def main():
    filenames = ['PMD8540804318002412548_s04_T1_REST_Frame_1__PCARDM1.dcm',
                 'PMD1907987506279511791_s08_T1_STRESS02_Frame_1__PCARDM1.dcm']
    dcms = [load_dcm(filepath(n)) for n in filenames]

    dcm_rest = dcms[0]
    img_rest = dcm_rest.pixel_array

    [print(f'{k}: {v}') for k, v in dcm_rest.items()]

    histogram = cv2.calcHist([img_rest.astype('float32')], [0], mask=None, histSize=[256], ranges=[0, 2**16])
    plt.subplot(121), plt.imshow(img_rest, cmap=plt.cm.bone)
    plt.subplot(122), plt.plot(histogram), plt.xticks(np.arange(0, 2**8+1, step=2**6), np.arange(0, 2**16+1, step=2**14), rotation=45)
    plt.show()


if __name__ == '__main__':
    main()
