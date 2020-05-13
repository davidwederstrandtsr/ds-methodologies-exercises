#!/usr/bin/env python
# coding: utf-8
# %% [markdown]
#
# Each scaler function should create the object, fit and transform both train and test. 
# They should return the scaler, train dataframe scaled, test dataframe scaled. 
# Be sure your indices represent the original indices from train\/test, as those represent the indices from the original dataframe. 
# Be sure to set a random state where applicable for reproducibility!
#  
# - **split_my_data(X, y, train_pct)**
# - **standard_scaler()**
# - **scale_inverse()**
# - **uniform_scaler()**
# - **gaussian_scaler()**
# - **min_max_scaler()**
# - **iqr_robust_scaler()**

# %%
import pandas as pd
import numpy as np
import sklearn.preprocessing

from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler
from sklearn.model_selection import train_test_split


# %% [markdown]
# ### Train Test Split
# - split the df into train and test
# - train will be used to develop the model
# - test will be used to ensure train_model efficiency

# %%
# this will return X_train, X_test, y_train, y_test
def split_my_data(X, y, train_pct):
    return train_test_split(X, y, test_size=train_pct)


# %% [markdown]
# ### Standard Scaler
# - Scale to Standard Normal Distribution (mean=0, stdev=1)

# %%
# standard_scaler returns the thing "fit"
def standard_scaler(train, test):
    # create standard scaler object & fit
    scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train)
    # transform train
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    # transform test
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    
    return train_scaled, test_scaled, scaler


# %% [raw]
#

# %% [markdown]
# ### Scale Inverse 
# - will return the df with its values reverted back to their original form
#

# %%
# revert the scaled back to original
def scale_inverse(train, test, scaler):
    # return to original values:
    train_unscaled = pd.DataFrame(scaler.inverse_transform(train), columns=train.columns.values).set_index([train.index.values])
    test_unscaled = pd.DataFrame(scaler.inverse_transform(test), columns=test.columns.values).set_index([test.index.values])
    
    return train_unscaled, test_unscaled


# %% [markdown]
#

# %%
def uniform_scaler(train, test):  
    # create uniform scaler object and fit to train
    scaler = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True).fit(train)
    # apply to train
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    # apply to test
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    
    return train_scaled, test_scaled, scaler


# %%
def gaussian_scaler(train, test):
    # create scaler object using yeo-johnson method and fit to train
    scaler = PowerTransformer(method='yeo-johnson', standardize=False, copy=True).fit(train)
    # apply to train
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    # apply to test
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

    return train_scaled, test_scaled, scaler


# %%
def min_max_scaler(train, test):
    # create scaler for the min and max 
    scaler = MinMaxScaler(copy=True, feature_range=(0,1)).fit(train)
    # apply to train
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    # apply to test
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

    return train_scaled, test_scaled, scaler


# %%
def iqr_robust_scaler(train, test):
    # create a robust scaler 
    scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(train)
    # apply to train
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    # apply to test
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

    return train_scaled, test_scaled, scaler

# %%
