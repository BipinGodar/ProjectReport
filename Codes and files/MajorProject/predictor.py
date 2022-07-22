import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pickle
import os

with open('model_pickle','rb') as f:
    mp=pickle.load(f)

mp.predict(data)