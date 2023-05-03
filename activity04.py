import random

import numpy as np
from scipy import ndimage
from skimage import io
from skimage.feature import canny
from skimage.filters import gabor_kernel

import typing as tp

import matplotlib.pyplot as plt


def apply_canny(img, sigma):
    """ Apply Canny edge detector to image. """
    # Your code here:
    #   See `skimage.feature.canny(...)`
    # ...
    return canny(img, sigma=sigma)


def visualize_img_and_edges(grayscale_image, edges_image):
    """ Visualize original image and edges. """
    # Your code here:
    #   Remember `plt.subplots(...)` and `plt.imshow(...)`.
    # ...
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(grayscale_image)
    ax2.imshow(edges_image)
    fig.show()


def create_filter_bank():
    """ Adapted from skimage documentation """
    kernels = []
    for theta in range(6):
        theta = theta / 4. * np.pi
        for sigma in (1, 3, 5):
            for frequency in (0.05, 0.15, 0.25):
                kernel = np.real(gabor_kernel(frequency, theta=theta,
                                              sigma_x=sigma, sigma_y=sigma))
                kernels.append(kernel)
    return kernels


def visualize_filter_bank(kernel1, kernel2, kernel3, kernel4, kernel5, kernel6):
    """ Visualize filter bank. """
    # Your code here:
    #   Remember `plt.subplots(...)` and `plt.imshow(...)`.
    # ...
    fig, axs = plt.subplots(2, 3)
    axs = [a for ax in axs for a in ax]
    fig.suptitle('Kernels')
    [ax.imshow(k)
     for k, ax in zip([kernel1, kernel2, kernel3, kernel4, kernel5, kernel6], axs)]
    fig.show()


def apply_filter(image, kernel):
    """ Apply linear filter to image. """
    # Your code here:
    #   See `ndimage.convolve(...)`
    # ...
    return ndimage.convolve(image, kernel, mode='reflect')  # Why mode='reflect'?


def get_marker(img: np.ndarray, position: tp.Tuple):
    """ Create a boolean mask of 0s, except for a 1 at the location `position`."""
    marker = np.empty_like(img)
    marker[position] = 1
    return marker


def image_data():
    """ Load image data. """
    data = [
        {
            'name': 'IMD002.bmp',
            'position_lesion': [500, 300],
            'position_skin': [50, 50],
            # To be loaded in the following:
            'img': None,
            'img_grayscale': None,
            'markers': None
        },
        {
            'name': 'IMD004.bmp',
            'position_lesion': [500, 300],
            'position_skin': [50, 50],
            # To be loaded in the following:
            'img': None,
            'img_grayscale': None,
            'markers': None
        },
        {
            'name': 'IMD006.bmp',
            'position_lesion': [500, 300],
            'position_skin': [50, 50],
            # To be loaded in the following:
            'img': None,
            'img_grayscale': None,
            'markers': None
        }
    ]
    for d in data:
        name = d['name']
        d['img'] = io.imread(f'data/{name}').astype('float')
        d['img_grayscale'] = d['img'][:, :, 0]
        marker_lesion = get_marker(d['img_grayscale'], d['position_lesion'])
        marker_skin = get_marker(d['img_grayscale'], d['position_skin'])
        d['markers'] = marker_lesion + 2 * marker_skin

    return data


if __name__ == '__main__':
    data = image_data()[0]
    img = data['img_grayscale']

    # Extract contours from images
    edges = []
    for s in [1, 5, 10, 20]:
        edges.append(apply_canny(img, sigma=s))
        visualize_img_and_edges(img, edges[-1])     # Visualize

    # Repeat the same for all images with a good sigma:
    for data in image_data():
        img = data['img_grayscale']
        edgs = apply_canny(img, sigma=15)
        visualize_img_and_edges(img, edgs)

    # Visualize kernels
    kernels = create_filter_bank()
    kernel_selection = random.sample(kernels, k=6)
    visualize_filter_bank(*kernel_selection)

    # Apply them to a 1-channel image:
    data = image_data()[0]
    img = data['img_grayscale']
    fig, axs = plt.subplots(2, 4)
    filtered_images = [apply_filter(img, kernel)
                       for kernel in kernel_selection]
    visualize_filter_bank(*kernel_selection)
