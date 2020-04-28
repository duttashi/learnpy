# objective: Exploratory Data Analysis with Pandas
# Specifically, read data with missing values, and clean the data
# Reference: https://www.kaggle.com/rtatman/data-cleaning-challenge-handling-missing-values/
# https://www.kaggle.com/dansbecker/handling-missing-values

import pandas as pd, numpy as np, seaborn as sns


# read the data in memory
df = pd.read_csv('../../data/aps_failure_training_set.csv', keep_default_na= True)
# replace the missing values coded as na with NAN
df = df.replace(to_replace= 'na', value= np.nan)
# print column names
print(df.columns)
# take a look at first few rows
print(df.sample(5))
# Count the missing values
missing_values_count = df.isnull().sum()
print(missing_values_count)
# print missing values in first 10 columns
print(missing_values_count[0:10])
# That seems like a lot! It might be helpful to see what percentage of the values in our dataset were missing to give us a better sense of the scale of this problem:
# how many total missing values do we have?
total_cells = np.product(df.shape)
total_missing = missing_values_count.sum()
# percent of data that is missing
print((total_missing/total_cells) * 100)

# Method 1: Remove all missing data
# remove all columns with at least one missing value
columns_with_na_dropped = df.dropna(axis=1)
print(columns_with_na_dropped.head()) # 5 columns with missing values

# just how much data did we lose?
print("Columns in original dataset: %d \n" % df.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

# Method 2: replace all NAs with 0
df = df.fillna(0)
# check if missing values still exist or not
missing_values_count = df.isnull().sum()
print(missing_values_count) # no missing values

# Method 3: Impute the missing data
from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
#data_with_imputed_values = my_imputer.fit_transform(df)
#print(df.describe)
# make copy to avoid changing original data (when Imputing)
new_data = df.copy()
# make new columns indicating what will be imputed
missing_cols = (col for col in new_data.columns
                if new_data[col].isnull.any()
                )
# for col in missing_cols:
#     new_data[col + '_was_missing'] = new_data[col].isnull()





