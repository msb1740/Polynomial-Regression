#import the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset

Dataset = pd.read_csv('Salary.csv')
x = Dataset.iloc[:, 1:-1].values
y = Dataset.iloc[:, 1].values
#print(x)
#print(y)

#training the linear regression model on the whole dataset

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

#Polynomial Features
#Y = b0 + b1*X1 + b2*X1^2 + b3*X1^3 + ... + bn*X1^n

# training the polynomial regression model on the whole dataset

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

# simple linear regression eq: 
# y = b0+b1*x1

# Multi linear Regression eq:
# Y=  b0+b1*x1+b2*x2....+bn*xn

# Polynomial Regression eq:
# Y = b0+b1*x1+b2*x1(power 2)......+bn*x1(power n)

#visualising the linear regression results
#plt.scatter(x, y, color = 'red')
#plt.plot(x, lin_reg.predict(x), color = 'blue')
#plt.title('Truth or Bluff(Linear Regression)')
#plt.xlabel('Position Level')
#plt.ylabel('Salary')
#plt.show()

#visualising the polynomial regression results

plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color = 'blue')
plt.title('Truth or Bluff(Ploynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()