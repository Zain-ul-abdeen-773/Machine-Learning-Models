# -*- coding: utf-8 -*-
"""Salary expectation based on Experience

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GVoYwlcDTDsTo1qmQGiFv4jDRuN89C-q
"""

import pandas as pd
import numpy as np

data=pd.read_csv('Salary.csv')

data.head()

data.columns

data.info()

data.describe()

data.isnull().any()

import matplotlib.pyplot as plt
import seaborn as sns

plt.plot(data['Salary'],data['YearsExperience'],color='red')
plt.xlabel('Salary')
plt.ylabel('Years Experience')
plt.title('Salary vs YearsExperience')
plt.show()

from sklearn.model_selection import train_test_split
x=data.drop('Salary',axis=1)
x

y=data['Salary']
y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression
L=LinearRegression()

L.fit(x_train,y_train)

y_pred=L.predict(x_test)

y_test

y_pred

print(L.score(x_test,y_test))