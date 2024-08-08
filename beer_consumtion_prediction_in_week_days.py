# -*- coding: utf-8 -*-
"""Beer Consumtion  prediction in Week days

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q-fiP7wYQsHfwayc4Tf0imub0Q1t0wpR
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import metrics

pip install sns

beer_data=pd.read_csv('Consumo_cerveja.csv')

beer_data.head()

beer_data.columns

beer_data.info()

beer_data.describe()

beer_data.shape

beer_data.isna().any()

beer_data.dropna(how='all',inplace=True)

beer_data.replace({',':'.'},regex=True,inplace=True)

beer_data['Data']=pd.to_datetime(beer_data['Data'])

beer_data.info()

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

beer_data['Day']=beer_data['Data'].apply(lambda x: days[x.weekday()])

beer_data.head()

beer_data.columns

import seaborn as sns
plt.figure(figsize=(10,5))
ax=sns.barplot(x='Day',y='Consumo de cerveja (litros)',data=beer_data,color='blue')
plt.ylabel('Consumtion (Liters)')
plt.show()

beer_data.drop(['Data','Day'],axis=1,inplace=True)

beer_data=beer_data.apply(pd.to_numeric)

beer_data.dtypes

beer_data

from sklearn.model_selection import train_test_split
x=beer_data.drop('Consumo de cerveja (litros)',axis=1)
y=beer_data['Consumo de cerveja (litros)']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression
L=LinearRegression()

L.fit(x_train,y_train)

y_pred=L.predict(x_test)

y_pred

y_test

print(L.score(x_test,y_test))