import pandas
from pandas import plotting
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, wilcoxon, bartlett, kstest, shapiro

import matplotlib.pyplot as plt

data = pandas.read_csv('data/brain_size.csv', sep=';', na_values=".")
print(f'Medidas: {data.shape}')
print(f'Columnas: {data.columns}')

plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])
plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])
plt.show()

female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
