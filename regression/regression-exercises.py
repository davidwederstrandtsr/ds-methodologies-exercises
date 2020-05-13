#!/usr/bin/env python
# coding: utf-8

import warnings
warnings.filterwarnings("ignore")

import env
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn.preprocessing
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from split_scale import split_my_data, standard_scaler, scale_inverse, uniform_scaler, gaussian_scaler, min_max_scaler, iqr_robust_scaler

from wrangle import wrangle_telco

df = wrangle_telco()

df.info()

print(df.columns[df.isnull().any()])

df.monthly_charges.value_counts(sort=True, ascending=True)

df.describe()

df.groupby('tenure').mean().plot.bar(figsize=(16,9), ec='black', width=.9)

col_names = ['customer_id', 'tenure', 'monthly_charges', 'total_charges']

X_train_scaled = df.copy()

X = df[['tenure', 'monthly_charges']]
y = df[['total_charges']]
train_pct = .25
X_train, X_test, y_train, y_test = split_my_data(X, y, train_pct)

assert X_train.shape[0] == y_train.shape[0]
assert X_test.shape[0] == y_test.shape[0]


# ### Standard Scaler
# $$x'={\frac {x-{\bar {x}}}{\sigma }}$$

X_train_standard_scaled, X_test_standard_scaled, standard_scaler = standard_scaler(X_train, X_test)

X_train_standard_scaled, X_test_standard_scaled

X_train_standard_scaled.head()


# ### Standard Scale Inverse

X_train_standard_unscaled, X_test_standard_unscaled = scale_inverse(X_train_standard_scaled, X_test_standard_scaled, standard_scaler)


X_train_standard_unscaled.head()


# ### Uniform Scaler
# 
# - It smooths out unusual distributions, and it spreads out the most frequent values and reduces the impact of (marginal) outliers →∴ a robust preprocessing scheme.
# 
# - It does distort correlations and distances within and across features.

X_train_uniform_scaled, X_test_uniform_scaled, uniform_scaler = uniform_scaler(X_train, X_test)
X_train_uniform_scaled.head()


# ### Uniform Scale Inverse

X_train_uniform_unscaled, X_test_uniform_unscaled = scale_inverse(X_train_uniform_scaled, X_test_uniform_scaled, uniform_scaler)
X_train_uniform_unscaled.head()


# ### Gaussian Scaler
# ##### Yeo-Johnson
# - supports both positive or negative data
# $$\begin{split}x_i^{(\lambda)} =
# \begin{cases}
#  [(x_i + 1)^\lambda - 1] / \lambda & \text{if } \lambda \neq 0, x_i \geq 0, \\[8pt]
# \ln{(x_i) + 1} & \text{if } \lambda = 0, x_i \geq 0 \\[8pt]
# -[(-x_i + 1)^{2 - \lambda} - 1] / (2 - \lambda) & \text{if } \lambda \neq 2, x_i < 0, \\[8pt]
#  - \ln (- x_i + 1) & \text{if } \lambda = 2, x_i < 0
# \end{cases}\end{split}$$
# 
# ##### Box-Cox
# - only supports positive data
# $$\begin{split}x_i^{(\lambda)} =
# \begin{cases}
# \dfrac{x_i^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0, \\[8pt]
# \ln{(x_i)} & \text{if } \lambda = 0,
# \end{cases}\end{split}$$

X_train_gaussian_scaled, X_test_gaussian_scaled, gaussian_scaler = gaussian_scaler(X_train, X_test)
X_train_gaussian_scaled.head()


# ### Gaussian Scale Inverse

X_train_gaussian_unscaled, X_test_gaussian_unscaled = scale_inverse(X_train_gaussian_scaled, X_test_gaussian_scaled, gaussian_scaler)
X_train_gaussian_unscaled.head()


# ### Min-Max Scaler
# 
# 
# $$x' = {\frac {x-{\text{min}}(x)}{{\text{max}}(x)-{\text{min}}(x)}}$$
# 
# $$x' = a+{\frac  {x-{\text{min}}(x))(b-a)}{{\text{max}}(x)-{\text{min}}(x)}}$$

X_train_min_max_scaled, X_test_min_max_scaled, min_max_scaler = min_max_scaler(X_train, X_test)
X_train_min_max_scaled.head()


# ### Min-Max Scale Inverse

X_train_min_max_unscaled, X_test_min_max_unscaled = scale_inverse(X_train_min_max_scaled, X_test_min_max_scaled, min_max_scaler)
X_train_min_max_unscaled.head()


# ### IRQ Robust Scaler
# - With a lot of outliers, scaling using the mean and variance is not going to work very well.
# 
# - Using RobustScaler, the median is removed (instead of mean) and data is scaled according to a quantile range (the IQR is default)

X_train_iqr_robust_scaled, X_test_iqr_robust_scaled, iqr_robust_scaler = iqr_robust_scaler(X_train, X_test)
X_train_iqr_robust_scaled.head()


# ### IRQ Robust Scale Inverse

X_train_iqr_robust_unscaled, X_test_iqr_robust_unscaled = scale_inverse(X_train_iqr_robust_scaled, X_test_iqr_robust_scaled, iqr_robust_scaler)
X_train_iqr_robust_unscaled.head()