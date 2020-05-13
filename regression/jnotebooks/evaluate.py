#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.formula.api import ols
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import explained_variance_score as evs

from math import sqrt


# In[2]:


def plot_residuals(y, yhat, df):
    sns.relplot(x=y, y=yhat, data=df)


# In[3]:



def regression_errors(actual, predicted):
 '''
 Takes in the actual and predicted values of y.
 Returns Sum of Squared Errors (SSE).
     Evaluated Sum of Squares (ESS),
     Total Sum of Squares (TSS),
     Mean Squared Error (MSE),
     Root Mean Squared Error (RMSE)
 '''
 SSE = mse(actual, predicted) * len(actual)
 ESS = sum((predicted - actual.mean()) ** 2)
 TSS = ESS + SSE
 MSE = mse(actual, predicted)
 RMSE = sqrt(MSE)
 
 return SSE, ESS, TSS, MSE, RMSE


# In[4]:


def baseline_mean_errors(actual, predicted_baseline):
    '''
    Takes in the actual values for u and the predicted baseline values for y.
    Returns the SSE, MSE, and RMSE for the baseline
    '''
    SSE_baseline = mse(actual, predicted_baseline) * len(actual)
    MSE_baseline = mse(actual, predicted_baseline)
    RMSE_baseline = sqrt(MSE_baseline)
    
    return SEE_baseline, MSE_baseline, RMSE_baseline


# In[5]:


def bettter_than_baeline(RMSE, RMSE_baseline):
    if RMSE < RMSE_baseline:
        print('Model is better than baseline')
    else:
        print('Baseline is better, need to look into different model')


# In[7]:


def model_significance(model, actual, predicted):
    '''
    Takes in a model, the actual y values, and the predicted y values.
    Calculates the significance of the model by comparing it's p-value to an
    alpha of 0.05.
    Prints out whether or not the model is significant.
    Returns the Explained Variance of Squares.
    '''
    p = model.f_pvalue
    alpha = 0.05
    
    EVS = evs(actual, predicted)
    
    if p < 0.05:
        print(f'p: {p} is less than alpha: {alpha}, therefore our model is significant.')
    else:
        print(f'p: {p} is more than alpha: {alpha}, therefore our model is not significant.')
    print('\n')
    print(f'EVS: {EVS}')
    return evs


# In[ ]:




