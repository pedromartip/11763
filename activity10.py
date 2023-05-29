import pandas
from pandas import plotting
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, wilcoxon, bartlett, kstest, shapiro

import matplotlib.pyplot as plt

from utils import filepath


def interpret_test(
        test_result,
        significance_level: float=0.01,
        null_hypothesis='Null hypothesis description',
        altv_hypothesis='Alternative hypothesis description'
        ):
    print(f'Test: {test_result.__class__.__name__}')
    print(f' >> H_0: {null_hypothesis}')
    print(f' >> H_1: {altv_hypothesis}')
    print(f' >> alpha: {significance_level:0.04f}')
    print(f' >> p-value: {test_result.pvalue:0.04f}')

    # YOUR CODE HERE:
    #   Set the value of `reject_null_hypothesis` to True or False, depending on the p-value and the significance level.
    # ...
    reject_null_hypothesis = False  # You might delete this line

    if reject_null_hypothesis:
        print(f'    >> We REJECT that "{null_hypothesis}".')
        print(f'    >> We DEDUCE that "{altv_hypothesis}".\n')
    else:
        print(f'    >> We DO NOT REJECT that "{null_hypothesis}".\n')


if __name__ == "__main__":
    # Load data
    dataset = pandas.read_csv(filepath('brain_size/dataset.csv'), sep=';', na_values=".")
    print(f'Measures: {dataset.shape}')
    print(f'Columns: {dataset.columns}')

    # Qualitative analysis of the dataset
    plotting.scatter_matrix(dataset[['Weight', 'Height', 'MRI_Count']])
    plotting.scatter_matrix(dataset[['PIQ', 'VIQ', 'FSIQ']])
    plt.show()

    # 1) Determine whether PIQ values follow a normal distribution.
    data = dataset['PIQ']
    res = shapiro(data)
    interpret_test(
        test_result=res,
        significance_level=0.10,
        null_hypothesis="PIQ values FOLLOW a normal distribution",
        altv_hypothesis="PIQ values DO NOT FOLLOW a normal distribution"
    )

    # 2) Determine wether PIQ and FSIQ are significantly different.
    # YOUR CODE HERE:
    #    Set the null hypothesis, the alternative hypothesis and the significance level.
    #    Choose the most appropriate test.
    #    Calculate the test, and interpret the result.
    # ...

    # 3) Determine wether a male's brain is significatively bigger in volume than a female's brain.
    # YOUR CODE HERE:
    #    Set the null hypothesis, the alternative hypothesis and the significance level.
    #    Choose the most appropriate test.
    #    Calculate the test, and interpret the result.
    # ...

    # 4) Determine wether a male's IQ and a female's IQ are significantly different
    # YOUR CODE HERE:
    #    Set the null hypothesis, the alternative hypothesis and the significance level.
    #    Choose the most appropriate test.
    #    Calculate the test, and interpret the result.
    # ...
