# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:38:24 2020
# reference: https://datascience.stackexchange.com/questions/81478/count-occurences-of-rows-based-one-cell-content-with-pandas
@author: Ashish
"""

import pandas as pd
from collections import Counter

df = pd.DataFrame([('A','01','prod_1'), 
                   ('A','01', 'prod_2'), 
                   ('A','02','prod_X'), 
                   ('B','05','prod_1'),
                   ('C','06','prod_2'),
                   ('C','06','prod_X')], 
                 columns=['customer', 'ordernum', 'product'])
#df.set_index('customer', inplace=True)
#df = df.rename_axis(None)
print (df)

val_count = df.groupby(['product','ordernum']).size()
print(val_count)
prod_order_count = df.groupby(['product', 'ordernum']).agg(Counter)
print(prod_order_count)
