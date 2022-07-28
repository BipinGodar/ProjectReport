import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os

df=pd.read_csv("car_data.csv")
df=pd.read_csv("train/")
# print(df.head())
# sizes=df['Attribute1'].value_counts(sort=1)   #counts the no. of data for each class/label
# print(sizes)



df.drop(['User ID'], axis=1, inplace=True) #Drop the irrelevant attribute

# print(df.head())
# df= df.dropna()  #If some data is missing it will drop the whole tuple

# #Convert non-numeric data to numeric
df.Gender[df.Gender=='Female']=0
df.Gender[df.Gender=='Male']=1


#Define dependent variable the output value that it should give
Y=df['Purchased'].values #values of the attribute column
Y=Y.astype('int') #changes the values to list of integers
# print(df.head())

# #Define independent variable, this value will include all flex sensor value
X=df.drop(labels=['Purchased'], axis=1)
# print(Y)
# print(df.head())

from sklearn.model_selection import train_test_split
# #Split Data into training and testing datasets
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=20)
# print(X_test)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=12, random_state=30)  #n-estimators no. of trees before selecting best tree
model.fit(X_train, Y_train)

prediction_test = model.predict(X_test)
from sklearn import metrics
print("Accuracy=",metrics.accuracy_score(Y_test,prediction_test))

import pickle
with open('model_pickle','wb') as f:
    pickle.dump(model,f)







