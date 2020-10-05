#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:40:39 2020

@author: ashleyraigosa
"""

# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import os


def callPolyModel(dateindex):
    # Importing the dataset
    dataset = pd.read_csv(os.path.join(
        os.environ['CARBONCHAT_DATA'], 'FinalDatasetNZ_1.csv'))
    X = dataset.iloc[:, 1:-1].values
    y = dataset.iloc[:, -1].values

    # Training the Linear Regression model on the whole dataset
    lin_reg = LinearRegression()
    lin_reg.fit(X, y)

    # Training the Polynomial Regression model on the whole dataset
    poly_reg = PolynomialFeatures(degree = 4)
    X_poly = poly_reg.fit_transform(X)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, y)

    # Visualising the Linear Regression results
    plt.scatter(X, y, color = 'red')
    plt.plot(X, lin_reg.predict(X), color = 'blue')
    plt.title('CO2 Prediction Based on Year')
    plt.xlabel('Year')
    plt.ylabel('CO2 (ppm)')
    plt.show()

    # Visualising the Polynomial Regression results
    plt.scatter(X, y, color = 'red')
    plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
    plt.title('CO2 Prediction Based on Year')
    plt.xlabel('Year')
    plt.ylabel('CO2 (ppm)')
    plt.show()

    # Visualising the Polynomial Regression results (for higher resolution and smoother curve)
    X_grid = np.arange(2015, 2020, 0.1)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X, y, color = 'red')
    plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
    plt.title('CO2 Prediction Based on Year')
    plt.xlabel('Year')
    plt.ylabel('CO2 (ppm)')
    plt.show()

    # Predicting a new result with Linear Regression
    # lin_reg.predict([[6.5]])
    lin_reg.predict([[dateindex]])

    # Predicting a new result with Polynomial Regression
    # lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
    return lin_reg_2.predict(poly_reg.fit_transform([[dateindex]]))