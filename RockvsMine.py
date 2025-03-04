# -*- coding: utf-8 -*-
"""Rock vs Mine.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kwDowugFsS3dzrLbuOIRC5l8yfM9zcTM

importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and Data processing"""

#loading the dataset to a pandas dataframe
sonar_data = pd.read_csv('/content/Copy of sonar data.csv',header=None)

sonar_data.head()

# number of rows and coloum
sonar_data.shape

sonar_data.describe() #describe ----> statistical measures of data

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#seprating data and labels
X = sonar_data.drop(columns=60,axis=1)
Y = sonar_data[60]

print(X)
print(Y)

"""Training and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

print(X_train)
print(Y_train)

"""Model training-->logistic regession"""

model = LogisticRegression()

#training logistic regression model with training data
model.fit(X_train, Y_train)

"""Model evaluation"""

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data : ' , training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data : ',test_data_accuracy)

"""Making a predictive system"""

input_data = (0.0526,0.0563,0.1219,0.1206,0.0246,0.1022,0.0539,0.0439,0.2291,0.1632,0.2544,0.2807,0.3011,0.3361,0.3024,0.2285,0.2910,0.1316,0.1151,0.3404,0.5562,0.6379,0.6553,0.7384,0.6534,0.5423,0.6877,0.7325,0.7726,0.8229,0.8787,0.9108,0.6705,0.6092,0.7505,0.4775,0.1666,0.3749,0.3776,0.2106,0.5886,0.5628,0.2577,0.5245,0.6149,0.5123,0.3385,0.1499,0.0546,0.0270,0.0380,0.0339,0.0149,0.0335,0.0376,0.0174,0.0132,0.0103,0.0364,0.0208)
#chainging a input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]=='R'):
  print('The object is a Rock')
else:
  print('The object is a Mine')

