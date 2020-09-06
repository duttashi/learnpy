# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:03:52 2020

@author: Ashish
"""

import pandas as pd
import os
print(os.getcwd())
df = pd.read_csv('data/heart_failure_clinical_records_dataset.csv', keep_default_na= True)
print(df.describe)
print(df.columns)
print(df.info())
print(df['DEATH_EVENT'])