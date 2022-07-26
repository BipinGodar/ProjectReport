import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pickle
import os
from playsound import playsound

data=[["0","80","45000"]]

with open('model_pickle','rb') as f:
    mp=pickle.load(f)

a=mp.predict(data)
r=a[0]
print(r)
if r==1:
    playsound('Hello.mp3')
else:
    playsound('Thank_You.mp3')