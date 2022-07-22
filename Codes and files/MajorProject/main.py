import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pickle
import os

df=pd.read_csv("excel_file.csv")
# print(df.head())
# sizes=df['Attribute1'].value_counts(sort=1)   #counts the no. of data for each class/label
# print(sizes)



df.drop(['Attribute to be Dropped'], axis=1, in_place=True) #Drop the irrelevant attribute

df= df.dropna()  #If some data is missing it will drop the whole tuple


#Convert non-numeric data to numeric
df.AttributeOP[df.AttributeOP=='Hello']=1
df.AttributeOP[df.AttributeOP=='Thank You']=2


#Define dependent variable the output value that it should give
Y=df['AttributeOP'].values #values of the attribute column
Y=Y.astype('int') #changes the values to list of integers

#Define independent variable, this value will include all flex sensor value
X=df.drop(labels=['AttributeOP'], axis=1)

#Split Data into training and testing datasets
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=20)
model = RandomForestClassifier(n_estimators=10, random_state=30)  #n-estimators no. of trees before selecting best tree
model.fit(X_train, Y_train)

prediction_test = model.predict(X_test)
print("Accuracy=",metrics.accuracy_score(Y_test,prediction_test))

with open('model_pickle','wb') as f:
    pickle.dump(model,f)







