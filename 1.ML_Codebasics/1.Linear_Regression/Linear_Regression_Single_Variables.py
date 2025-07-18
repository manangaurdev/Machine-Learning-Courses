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