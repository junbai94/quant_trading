# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:53:29 2017

@author: junbai

Learning better linear regression
"""

import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split

data = pd.read_csv('C:/Users/j291414/Desktop/Advertising.csv', index_col=0)

lm1 = smf.ols(formula="sales ~ TV", data=data).fit()

print lm1.params
print

X_new = pd.DataFrame({'TV': [50]})
print lm1.predict(X_new)

sns.pairplot(data, x_vars=['TV','radio','newspaper'], y_vars='sales',  kind='reg')

print 
print lm1.conf_int()

print 
print lm1.pvalues

lm2 = smf.ols(formula="sales ~ TV + radio + newspaper", data=data).fit()
print
print lm2.params

print lm2.summary()

lm3 = smf.ols(formula="sales ~ TV + radio", data=data).fit()
print lm3.summary()


# include Newspaper
X = data[['TV', 'radio', 'newspaper']]
y = data.sales

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Instantiate model
lm2 = LinearRegression()

# Fit Model
lm2.fit(X_train, y_train)

# Predict
y_pred = lm2.predict(X_test)

# RMSE
print
print ("RMSE:")
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))