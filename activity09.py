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
    true_negatives = 0
    true_positives = 0
    false_negatives = 0
    false_positives = 0
    # Your code here:
    #   ...

    return true_positives, true_negatives, false_positives, false_negatives


def perimage_performance_measures(
        mask_reference: np.ndarray,
        mask_prediction: np.ndarray
        ) -> tuple[float, float, float]:
    """ Compute the sensitivity, specificity and f1_score from two boolean masks. """
    sensitivity = 0
    specificity = 0
    f1_score = 0
    # Your code here:
    #   ...

    return sensitivity, specificity, f1_score


def hypothesis_testing(
        name_method_A: str,
        name_method_B: str
        ) -> float:
    """ Returns the p-value of a hypothesis test to determine if segmentation A is statistically superior to segmentation B."""
    images_gt = [load_single_segmentation('GroundTruth01', idx) for idx in range(1, 21)]
    # Your code here: load all images and evaluate it according to the corresponding ground truth
    #   Which is a better performance measure: sensitivity, specificity or f1_score?
    #   ...

    # Your code here: perform the hypothesis test of whether one measure is statistically superior to the other
    #   Consider the wilcoxon signed-rank test (why?), see `scipy.stats.wilcoxon(...)`
    #   Return the p-value of the corresponding test
    #   ...


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
    print(f'  >> Result:   {tp} TP, {tn} TN, {fp} FP, {fn} FN')
    print(f'  >> Expected: 21483 TP, 294039 TN, 6481 FP, 7957 FN.')

    # Image-level performance measures
    sen, spe, fsc = perimage_performance_measures(
        load_single_segmentation(method_A, idx_sample),
        load_single_segmentation(method_B, idx_sample)
    )
    print(f'Per-image performance measures: {method_A} vs. {method_B}, sample nº{idx_sample}')
    print(f'  >> Result:   {sen:.02%} sensitivity, {spe:.02%} specificity, {fsc:.02%} f1_score')
    print(f'  >> Expected: 72.97% sensitivity, 97.84% specificity, 74.85% f1_score.')

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
    method_A = 'Prediction2004Staal'
    method_B = 'Prediction2004Niemeijer'
    pvalue = hypothesis_testing(
        method_A,
        method_B
    )
    print(f'Hypothesis testing: {method_A} vs. {method_B}')
    print(f'  >> Result:   p-value = {pvalue:.04f}.')
    print(f'  >> Expected: p-value = 0.0413.')

    # Hypothesis testing: All vs all
    print(f'Hypothesis testing: All vs all.')
    for method_A in SEGMENTATION_METHODS[1:]:
        for method_B in SEGMENTATION_METHODS[1:]:
            if method_A != method_B:
                pvalue = hypothesis_testing(method_A, method_B)
                if pvalue < 0.05:
                    print(f'  >> {method_A} is statistically better than {method_B} (p-value: {pvalue:.04f})')
