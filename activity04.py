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
    return canny(img, sigma)


def visualize_img_and_edges(grayscale_image, edges_image):
    """ Visualize original image and edges. """
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1), plt.imshow(grayscale_image, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 2, 2), plt.imshow(edges_image, cmap='gray')
    plt.title('Edges')
    plt.show()



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


def visualize_filter_bank(*kernels):
    ''' *kernels --> Tots els param que me fiquis, me'ls fica amb un array'''
    plt.figure(figsize=(12, 8))
    
    for i, kernel in enumerate(kernels, 1):
        plt.subplot(2, 3, i)
        plt.imshow(kernel, cmap='gray')
        plt.title(f'Kernel {i}')
    plt.show()


def apply_filter(image, kernel):
    """ Apply linear filter to image. """
    return ndimage.convolve(image, kernel)


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
    visualize_filter_bank(*filtered_images)
