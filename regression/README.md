# REGRESSION

>## Acquire and Prep

### wrangle.py

#### this file contains the wrangle_telco function

- the function takes no arguments
- read in sql and creates a dataframe
- cleans the data

---

>## Scaling Numeric Data

### *split_scale.py*

#### this file contains the following functions

##### **split_my_data(X, y, train_pct)**

- this function will return X_train, X_test, y_train, y_test

##### **standard_scaler()**

- Scale to Standard Normal Distribution (mean=0, stdev=1)

##### **scale_inverse()**

- will return the df with its values reverted back to their original form

##### **uniform_scaler()**

- It smooths out unusual distributions, and it spreads out the most frequent values and reduces the impact of (marginal) outliers →∴ a robust preprocessing scheme.

##### **gaussian_scaler()**

- This uses either the Box-Cox or Yeo-Johnson method to transform to resemble normal or standard normal distrubtion.
- It defaults to zero-mean and unit-variance (standard normal).

###### Yeo-Johnson

- supports both positive or negative data

###### Box-Cox

- only supports positive data

##### **min_max_scaler()**

- This is a linear transformation since it is derived from a linear function.
- Values will lie between a given minimum and maximum value, such as 0 and 1.

##### **iqr_robust_scaler()**

- With a lot of outliers, scaling using the mean and variance is not going to work very well.
- Using RobustScaler, the median is removed (instead of mean) and data is scaled according to a quantile range (the IQR is default)


