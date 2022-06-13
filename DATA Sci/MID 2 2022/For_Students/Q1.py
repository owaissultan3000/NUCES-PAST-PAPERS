# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

#gathering the data
df = pd.read_csv('dataset.csv')

print(df.head()) 

# print the number of rows and columns


# print name of columns that have no missing values


# print name of columns that have  missing values
#print(no_nulls)

print(df.describe()) # what is the purpose?
print(df.info()) # what is the purpose?

#help(pd.Series.nunique)

# discover the number of unique values of categorical columns


# How many hosts are in every neighbourhood_group? 
# help(pd.value_counts)


# Which Id has the most expensive property? 


#removing the last_review column




