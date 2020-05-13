#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from pandas_profiling import ProfileReport
from pydataset import data
import matplotlib.pyplot as plt


# to run report
# 
# - profile = ProfileReport(df, title='Pandas Profiling Report', html={'style':{'full_width':True}})

# In[2]:


def plot_variable_pairs(df, hue=None):
    g = sns.pairplot(df, hue=hue, kind="reg", corner=True, diag_kind="kde",
        plot_kws=({'line_kws':{'color':'red'}, 'scatter_kws':{'alpha':0.7}}))
    g.fig.suptitle("Scattlerplot with Regression for Continuous Variables")
    plt.show()


# ## Exercise 2
# - write a function, months_to_years(tenure_months, df) that returns your dataframe with a new feature tenure_years, in complete years as a customer.

# In[3]:


def months_to_years(n_months, df,rounding=False):
    """
    Returns the dataframe with a new column providing years.
    Rounding rounds up or down, defaults to highest complete year.
    For example, life insurence underwrites round up/down while tenure based bouns
       conversions take the highest wholenumber w/o rounding
    """
    if rounding:
        df["teunre_years"] = np.round(n_months / 12)
        return df
    else:
        df["tenure_years"] = n_months // 12
        return df


# ## Exercise 3
# 
# - Write a function, plot_categorical_and_continuous_vars(categorical_var, continuous_var, df), that outputs 3 different plots for plotting a categorical variable with a continuous variable, e.g. tenure_years with total_charges. For ideas on effective ways to visualize categorical with continuous: https://datavizcatalogue.com/. 
# - You can then look into seaborn and matplotlib documentation for ways to create plots.

# In[4]:


def plot_categroical_and_continous_vars(categorical_var, continuous_var, df):
    sns.catplot(y=categorical_var, x=continuous_var, data=df)
    sns.catplot(x=continuous_var, kind="count", palette="ch:.25", data=df)
    sns.catplot(y=categorical_var, x=continuous_var, kind="box", data=df)
    sns.catplot(y=categorical_var, x=continuous_var, kind="violin", bw=.15, cut=0, data=df)


# In[ ]:




