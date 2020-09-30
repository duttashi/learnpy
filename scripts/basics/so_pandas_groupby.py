# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:38:24 2020
# reference: https://datascience.stackexchange.com/questions/81478/count-occurences-of-rows-based-one-cell-content-with-pandas
@author: Ashish
"""

import pandas as pd
# from collections import Counter

df = pd.DataFrame([('A','01','prod_1'), 
                   ('A','01', 'prod_2'), 
                   ('A','02','prod_X'), 
                   ('B','05','prod_1'),
                   ('C','06','prod_2'),
                   ('C','06','prod_X')], 
                 columns=['customer', 'ordernum', 'product'])
#df.set_index('customer', inplace=True)
#df = df.rename_axis(None)
# print (df)

# val_count = df.groupby(['product','ordernum']).size()
# print(val_count)
# prod_order_count = df.groupby(['product', 'ordernum']).agg(Counter)
# print(prod_order_count)
# df['counter']=1
# val_count = df.groupby(['product'])['counter'].sum()
# print(val_count)
# g = df.groupby(['product','ordernum']).size().to_frame('ordercount').reset_index()
# print(g)

# from itertools import product
# combs = pd.DataFrame(list(product(df['product'], df['ordernum'])), 
#                      columns=['product', 'ordernum'])
# print(combs)

# result = g.merge(combs, how = 'right').fillna(0)
# print(result)

from itertools import combinations

def combine(batch):
    """Combine all products within one batch into pairs"""
    return pd.Series(list(combinations(set(batch), 2)))

df_combs = df.groupby('product')['customer'].apply(combine).value_counts()
# print(edges)
# edges = edges.reset_index()
# edges = pd.concat([edges, edges['index'].apply(pd.Series)], axis=1)
# edges.drop(['index'], axis=1, inplace=True)
df_combs.columns = 'combinations','count_values'
df_new = pd.DataFrame(df_combs)
print(df)
print(df_new)

