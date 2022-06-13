# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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


Data = {
   'Attribute1' : [2, 10, np.nan,  0,   2,      9,   -4,     -10,  0,  5 ],
    'Attribute2' :[3, 30, 16,     11,   np.nan, 13,   15,     11,  12, 15],
 'Attribute3' :[3, 87, 45,     34,   56,     44,   22,     66,  77, np.nan],
'Attribute4' : [2, 15, 3,       18,  8,      9,    np.nan,  2,  5,  9],
'label': [1, 0,  0,       0,   1,      1,    1,       0,  1,  0]
}


df = pd.DataFrame(Data) 

# Replace nan with 0 [0.5 Points]
# your code


data = df.iloc[:,0:4]
label = df.iloc[:,4]

#print(data)
#print(label)


# Split data into training / test. USe test size = 0.3, random state = 25 [0.25 Points]
# your code


# print the size of training and testing examples in here [0.25 Points]
# your code

# Train Classifiers Decision Tree, Neural Network, and SVM [0.75 Point]
# your code

# Test Classifiers Decision Tree Classifier, Neural Network, 1NN and SVM [0.75 Point]
# your code

# print accuraies obtained from each model [0.5 Point]
# your code


# plot ROC curve obtained from each model and explain results in your own words [1 Point]
# your code
#help(metrics.plot_roc_curve)






  




