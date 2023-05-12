import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pydicom
from skimage.morphology import binary_dilation, binary_erosion

from utils import filepath


def mean_absolute_error(img_input: np.ndarray, img_reference) -> np.ndarray:
    """ Compute the MAE between two images. """
    # Your code here:
    #   ...
    return np.mean(np.abs(img_input - img_reference))


def mean_squared_error(img_input: np.ndarray, img_reference) -> np.ndarray:
    """ Compute the MSE between two images. """
    # Your code here:
    #   ...
    return np.mean((img_input - img_reference)**2)


def mutual_information(img_input: np.ndarray, img_reference) -> np.ndarray:
    """ Compute the Shannon Mutual Information between two images. """
    # Your code here:
    #   ...
    nbins = [10, 10]
    # Compute entropy of each image
    hist = np.histogram(img_input.ravel(), bins=nbins[0])[0]
    prob_distr = hist / np.sum(hist)
    entropy_input = -np.sum(prob_distr * np.log2(prob_distr + 1e-7))  # Why +1e-7?
    hist = np.histogram(img_reference.ravel(), bins=nbins[0])[0]
    prob_distr = hist / np.sum(hist)
    entropy_reference = -np.sum(prob_distr * np.log2(prob_distr + 1e-7))  # Why +1e-7?
    # Compute joint entropy
    joint_hist = np.histogram2d(img_input.ravel(), img_reference.ravel(), bins=nbins)[0]
    prob_distr = joint_hist / np.sum(joint_hist)
    joint_entropy = -np.sum(prob_distr * np.log2(prob_distr + 1e-7))
    # Compute mutual information
    return entropy_input + entropy_reference - joint_entropy


if __name__ == '__main__':
    # Load data
    filenames = ['PCARDM1_T1_Rest.dcm',
                 'PCARDM1_T1_Stress.dcm']
    dcms = [pydicom.dcmread(filepath(n)) for n in filenames]
    imgs = [d.pixel_array for d in dcms]

    # Visualize
    fig, axs = plt.subplots(1, 3)
    axs[0].imshow(imgs[0], cmap='bone')
    axs[0].set_title('Image 1')
    axs[1].imshow(imgs[0] - imgs[1], cmap='bone')
    axs[1].set_title('Difference')
    axs[2].imshow(imgs[1], cmap='bone')
    axs[2].set_title('Image 2')
    fig.show()

    # Compute metrics
    mae = mean_absolute_error(imgs[0], imgs[1])
    print('MAE:')
    print(f'  >> Result: {mae:.02f} HU')
    print(f'  >> Expected: 927.75 HU')

    mse = mean_squared_error(imgs[0], imgs[1])
    print('MSE:')
    print(f'  >> Result: {mse:.02f} HU^2')
    print(f'  >> Expected: 919.08 HU^2')

    mutual_inf = mutual_information(imgs[0], imgs[1])
    print('Mutual Information:')
    print(f'  >> Result: {mutual_inf:02f} bits')
    print(f'  >> Expected value heavily depends on the discretization of the images.')
