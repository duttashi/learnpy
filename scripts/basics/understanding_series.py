# objective: Understanding Series - a python data structure
# script create date: 24/Feb/2020
# important points to remember
## A Series is a one-dimensional array
import pandas as pd
obj = pd.Series([4,10,'abc',20])
print(obj)
print(obj.values)
print(obj.index)

# create a series with a defined index
obj = pd.Series(data=[4,10,"abc",200], index=['1','2','3','4'])
print(obj)
# altering a series index
obj.index = ['a','b','c','4']
print(obj)
