# -*- coding: utf-8 -*-
"""Student Grade prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c0WSygjVu7Yfi9cvI0qXZ8PPqd3W0caF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_student=pd.read_csv("student-mat.csv")

data_student.head()

data_student['G3'].describe()

plt.hist(data_student['G3'], bins=20, edgecolor='black',color='blue')
plt.title('Distribution of Final grade of Students',fontsize = 25)
plt.xlabel('Final Grade',fontsize=20)
plt.ylabel('Count',fontsize=20)
plt.show()

data_student.info()

data_student.describe()

data_student.isnull().any()

data_student.columns

data_student.describe()
data_student.shape

male=len(data_student[data_student['sex']=='M'])
female=len(data_student[data_student['sex']=='F'])
print("Number of Male Students:",male)
print("Number of Female Students:",female)

data_student['GradeAvg']=(data_student['G1']+data_student['G2']+data_student['G3'])/3

def find_grade(data_student):
  grades=[]
  for row in data_student['GradeAvg']:
    if row>= (0.9 * data_student['GradeAvg'].max()):
      grades.append('A')
    elif row>= (0.7 * data_student['GradeAvg'].max()):
      grades.append('B')
    elif row < (0.7 * data_student['GradeAvg'].max()):
      grades.append('C')
  data_student['Grade']=grades
  return data_student

data_dum=find_grade(data_student)

data_dum.drop(['school','age'],axis=1,inplace=True)

data_dum.head()

d={'yes':1,'no':0}
data_dum['internet']=data_dum['internet'].map(d)
data_dum['romantic']=data_dum['romantic'].map(d)
data_dum['paid']=data_dum['paid'].map(d)
data_dum['higher']=data_dum['higher'].map(d)
data_dum['famsup']=data_dum['famsup'].map(d)
data_dum['nursery']=data_dum['nursery'].map(d)
data_dum['schoolsup']=data_dum['schoolsup'].map(d)
data_dum['activities']=data_dum['activities'].map(d)

d={'F':1,'M':0}
data_dum['sex']=data_dum['sex'].map(d)

data_dum.columns

from sklearn.model_selection import train_test_split
x=data_dum.drop("G3",axis=1)
y=data_dum["G3"]

data_dum.dtypes
#data_dum.to_csv('data_dum.csv', index=False

data_dum['G3']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)

from sklearn.linear_model import LinearRegression

L=LinearRegression()

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Identify categorical columns
categorical_cols = x_train.select_dtypes(include=['object']).columns

# Create a ColumnTransformer to handle categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ],
    remainder='passthrough'  # Keep numerical columns as they are
)

# Apply the preprocessing to your training and test data
x_train_encoded = preprocessor.fit_transform(x_train)
x_test_encoded = preprocessor.transform(x_test)

# Now, try fitting the model again
L.fit(x_train_encoded, y_train)

y_pred=L.predict(x_test_encoded)

print(L.score(x_test_encoded,y_test))