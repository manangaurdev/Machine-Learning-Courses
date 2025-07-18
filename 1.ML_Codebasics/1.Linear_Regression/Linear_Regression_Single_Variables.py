"""
Machine Learning is a set of techniques to make computer better at doing things that
humans (traditionally) can do better than machines

"""
# Task-0:- Importing necessay packages and required "homeprices.csv" file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("homeprices.csv")
df


# Task-1:- Analysing the dataset and understanding the relationship between 'area' and 'price' of the house
plt.xlabel('area(sqr ft)')
plt.ylabel('price(US$)')
plt.scatter(df.area, df.price, color='red', marker='+')


# Task-2:- Training my Linear Regression model for predicting the house prices
reg = linear_model.LinearRegression()
reg.fit(df[['area']], df['price'])

reg.predict([[3300]])

reg.coef_

reg.intercept_


d = pd.read_csv('area.csv')

p = reg.predict(d[['area']])

d['prices'] = p

d.to_csv("predicted_prices.csv")