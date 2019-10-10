#RavioliRegress AML 2019

#All the code has to be rewritten properly and optimized

import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model, preprocessing
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

X_t = pd.read_csv('task1/results/X_inliners.csv', ',')
y_t = pd.read_csv('task1/results/y_inliners.csv', ',')

# We will add feature selection here

# First of all we observe the effects of standardization/regularization on linear models
# Most likely the standardized model has a slightly better performance


scaler = preprocessing.StandardScaler().fit(X_t)
X_t_s =  X_t
X_t_s = scaler.transform(X_t_s) # X_t_s has now been scaled

print(X_t)
print(X_t_s)

regr = linear_model.LinearRegression()

cv_results = cross_validate(regr, X_t, y_t, cv=5);

print("Evaluating effects of standardization")
print("Score without standardization")
print(cv_results['test_score'])
print("Average: " + str(np.average(cv_results['test_score'])))

cv_results = cross_validate(regr, X_t_s, y_t, cv=5);
print("Score with standardization")
print(cv_results['test_score'])
print("Average: " + str(np.average(cv_results['test_score'])))

# Then we train each model (different parameters) and compute the cross validation score (with or without standardization
print("Trying out linear models")

arr = [linear_model.LinearRegression(), linear_model.Lasso(), linear_model.Ridge(), linear_model.ElasticNet()]

for model in arr:
    cv_results = cross_validate(model, X_t_s, y_t);
    print('Score of ' + str(model) + ': ')
    print(cv_results['test_score'])
    print("Average: " + str(np.average(cv_results['test_score'])))

for i in range (2, 5):
    print("Trying out polynomial models of degree " + str(i))
    poly = PolynomialFeatures(i)
    X_t_m = X_t_s
    poly.fit_transform(X_t_m)
    cv_results = cross_validate(model, X_t_s, y_t);
    print('Score of ' + str(model) + 'of degree ' + str(i) + ': ')
    print(cv_results['test_score'])
    print("Average: " + str(np.average(cv_results['test_score'])))

# We choose the right model and adjust the hyeprparameters