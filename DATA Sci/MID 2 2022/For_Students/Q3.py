# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:25:52 2022

@author: Waqas FAST NUCES
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn import tree
from sklearn.metrics import plot_confusion_matrix
from sklearn.neural_network import MLPClassifier
#from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC            #help(sklearn.svm.SVC)
import matplotlib.pyplot as plt
from sklearn import  metrics
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

########### Do not Remove These Lines#####
X_test = pd.read_csv('X_test.csv')
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')
y_test = pd.read_csv('y_test.csv')

X_train = X_train.iloc[:,1:]
X_test = X_test.iloc[:,1:]
y_test = y_test['label']
y_train = y_train['label']


# perform Kmean clustering with 2 clusters on training data only and find centroids [1.5 Points]
# your code


# repalce all zero values in both train and test examples by corespoding elements of first centroid [1.5 Points]
# see Q3_details.jpg for more help in the downloaded folder 

# your code 





# Use StandardScalar to scale trianing and testing data [1 Point]
# your code


# Copy and Paste from Q2; No need to write again in the answer sheet
# Train Classifiers Decision Tree, Neural Network, and SVM [0.75 Point]
# your code

# Test Classifiers Decision Tree Classifier, Neural Network, 1NN and SVM [0.75 Point]
# your code

# print accuraies obtained from each model [0.5 Point]
# your code


# plot ROC curve obtained from each model and explain results in your own words [1 Point]
# your code











  






  





