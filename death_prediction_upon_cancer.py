# -*- coding: utf-8 -*-
"""Death prediction upon Cancer

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qcoFzdzokLXs_0BmT4mR6fl6-NxVtC8g
"""

import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('Risk of Developing or Dying From Cancer.csv')

data.head()

data

data.tail()

data.info()

data.columns

data.describe()

data.shape

data.isnull().any()

data.isnull().sum()

plt.scatter(data['Male Risk Development Percentage'],data['Male Risk Dying Percentage'],color='blue',edgecolors='black')
plt.xlabel(' Risk Development Percentage')
plt.ylabel(' Risk Dying Percentage')
plt.figsize=(5,5)
plt.xlim(0,20)
plt.ylim(0,20)
plt.title(' Risk Development Percentage vs  Risk Dying Percentage')
plt.show()

data['Male Risk Dying Percentage'].head()

data['Male Risk Development Percentage'].head()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Assuming 'data' is your DataFrame
x = data.drop('Male Risk Dying Percentage', axis=1)
y = data['Male Risk Dying Percentage']

# Convert string columns to numerical using one-hot encoding
x = pd.get_dummies(x)  # This will handle string columns like 'Male Risk Development Percentage'

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

L = LinearRegression()
L.fit(x_train, y_train)  # This should now work without the ValueError

y_pred=L.predict(x_test)

y_test

y_pred

print(L.score(x_test,y_test))