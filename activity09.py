import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import wilcoxon
from skimage.io import imread

from utils import filepath

SEGMENTATION_METHODS = [
    'GroundTruth01',
    'GroundTruth02',
    'Prediction1989Chaud',
    'Prediction1999Perez',
    'Prediction2001Zana',
    'Prediction2003Jiang',
    'Prediction2004Niemeijer',
    'Prediction2004Staal',
    'Prediction2008Soares',
    'Prediction2015Roychowdhury',
]


def load_single_segmentation(method, idx):
    """ Load a single segmentation mask from the DRIVE dataset, returning it as a boolean 2D image. """
    path = filepath(f'EyeFundus_DRIVE/{method}/')
    fname = [n for n in os.listdir(path) if n.startswith(f'{idx:02d}')][0]
    img = imread(f'{path}{fname}')
    img = img > np.median(img)
    if img.ndim == 3:
        img = np.max(img[:, :, :3], axis=-1)
    return img


def perpixel_performance_measures(
        mask_reference: np.ndarray,
        mask_prediction: np.ndarray
        ) -> tuple[int, int, int, int]:
    """ Compute the number of true/false positives and true/false negatives from two boolean masks."""
    # Your code here:
    #   ...
    true_negatives = np.sum((mask_reference == 0) & (mask_prediction == 0))
    true_positives = np.sum((mask_reference == 1) & (mask_prediction == 1))
    false_negatives = np.sum((mask_reference == 1) & (mask_prediction == 0))
    false_positives = np.sum((mask_reference == 0) & (mask_prediction == 1))
    return true_positives, true_negatives, false_positives, false_negatives


def perimage_performance_measures(mask_reference, mask_prediction):
    """ Compute the sensitivity, specificity and f1_score from two boolean masks. """
    # Your code here:
    #   ...
    tp, tn, fp, fn = perpixel_performance_measures(mask_reference, mask_prediction)
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    f1_score = 2 * tp / (2 * tp + fp + fn)
    return sensitivity, specificity, f1_score


def hypothesis_testing(name_method_A: str, name_method_B: str) -> float:
    """ Returns the p-value of a hypothesis test to determine if segmentation A is statistically superior to segmentation B."""
    images_gt = [load_single_segmentation('GroundTruth01', idx) for idx in range(1, 21)]
    # Your code here: load all images and evaluate it according to the corresponding ground truth
    #   Which is a better performance measure: sensitivity, specificity or f1_score?
    #   ...
    images_A = [load_single_segmentation(name_method_A, idx) for idx in range(1, 21)]
    measures_A = [
        perimage_performance_measures(gt, pred)[2]  # Why [2]?
        for gt, pred in zip(images_gt, images_A)
    ]
    images_B = [load_single_segmentation(name_method_B, idx) for idx in range(1, 21)]
    measures_B = [
        perimage_performance_measures(gt, pred)[2]
        for gt, pred in zip(images_gt, images_B)
    ]

    # Your code here: perform the hypothesis test of whether one measure is statistically superior to the other
    #   Consider the wilcoxon signed-rank test (why?), see `scipy.stats.wilcoxon(...)`
    #   ...
    test = wilcoxon(measures_A, measures_B, alternative='greater')
    return test.pvalue


if __name__ == '__main__':
    # Visualize samples
    fig, axes = plt.subplots(2, 5)
    plt.suptitle('Different segmentation masks')
    for method, ax in zip(SEGMENTATION_METHODS, axes.ravel()):
        ax.imshow(load_single_segmentation(method, 1))
        ax.set_title(method[14:] if method.startswith('Prediction') else f'GT{method[11:]}')
    plt.show()

    # Pixelwise performance measures
    method_A = 'GroundTruth01'
    method_B = 'Prediction2015Roychowdhury'
    idx_sample = 1
    tp, tn, fp, fn = perpixel_performance_measures(
        load_single_segmentation(method_A, idx_sample),
        load_single_segmentation(method_B, idx_sample)
    )
    print(f'Per-pixel performance measures: {method_A} vs. {method_B}, sample nº{idx_sample}')
    print(f'  >> Result: {tp} TP, {tn} TN, {fp} FP, {fn} FN')
    print(f'  >> Expected: TODO.')

    # Image-level performance measures
    sen, spe, fsc = perimage_performance_measures(
        load_single_segmentation(method_A, idx_sample),
        load_single_segmentation(method_B, idx_sample)
    )
    print(f'Per-image performance measures: {method_A} vs. {method_B}, sample nº{idx_sample}')
    print(f'  >> Result: {sen:.02%} sensitivity, {spe:.02%} specificity, {fsc:.02%} f1_score')
    print(f'  >> Expected: TODO.')

    # Visualize some images
    fig, axs = plt.subplots(2, 4)
    fig.suptitle(f'F1-score: {method_A} vs. {method_B}')
    for idx in range(1, 5):
        axs[0, idx - 1].imshow(load_single_segmentation(method_A, idx))
        axs[1, idx - 1].imshow(load_single_segmentation(method_B, idx))
        _, _, fscore = perimage_performance_measures(
            load_single_segmentation(method_A, idx), load_single_segmentation(method_B, idx)
        )
        axs[0, idx - 1].set_title(f'{fscore:.02%}')
    plt.show()

    # Hypothesis testing
    pvalue = hypothesis_testing(
        method_A,
        method_B
    )
    print(f'Hypothesis testing: {method_A} vs. {method_B}')
    print(f'  >> Result: {pvalue:.02%} p-value.')
    print(f'  >> Expected: TODO.')

    # Visualize all methods
    for method_A in SEGMENTATION_METHODS[1:]:
        for method_B in SEGMENTATION_METHODS[1:]:
            if method_A != method_B:
                pvalue = hypothesis_testing(method_A, method_B)
                print(f'Hypothesis testing: {method_A} better than {method_B}? -> p-value: {pvalue:.02%}.')
                if pvalue < 0.05:
                    print(f'  >> {method_A} is statistically better than {method_B}!')