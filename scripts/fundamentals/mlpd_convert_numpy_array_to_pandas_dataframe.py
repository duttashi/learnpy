# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:18:29 2020
Obkective: create pandas dataframe using numpy array
@author: Ashish
"""
import numpy as np
import pandas as pd

temp = np.random.randint(low=20, high=100, size=[20,])
names = np.random.choice(['Brad','Sam','Pitts','Justin'], 20)
random = np.random.choice([10,11,12,13,14],20)

# zip the above variables into a list and create dataframe
a = list(zip(temp,names,random))
df = pd.DataFrame(a, columns=['temp','names','random'])
print(df)

# create dataframe using dictionary
df = pd.DataFrame({'temp':temp,'names':names,'random':random})
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.names)
print(df.temp)
print(df.temp.describe())
print(df.values)

df.set_index('temp', inplace= True)
print(df)
df.sort_index(axis=0, ascending=False)
print(df)
df.sort_values(by='random', ascending= True)
print(df)

# drop a column, set axis=1
print(df.columns)
print(df.drop(['random'], axis=1))
print(df.head())
# print(df.drop(['random'], axis=1, inplace=True))
# print(df.head())
print(df.iloc[0,:])
print(df.loc[(df.random >11) & (df.random <14),:])

# create a function
def highRandom(x):
    return x>11

# Now lets the apply function to create a custom column in the dataframe
df1= df
df1['highRandom'] = df1['random'].apply(highRandom)
print(df1)
