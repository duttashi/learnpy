# objective: Exploratory Data Analysis with Pandas
# script create date: 24/Feb/2020

# reference: https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python
# load required libraries
import pandas as pd, numpy as np, seaborn as sns, matplotlib.pyplot as plt
# read the data in memory
df_train = pd.read_csv('../../data/train_hp.csv', keep_default_na= True)
df_test = pd.read_csv('../../data/test_hp.csv', keep_default_na= True)

# column names
# print(df_train.columns)
# print column name and dat types
print(df_train.info())
# describe the response variable
x = df_train['SalePrice'].describe()
#print(x)
# show the plot
# Histogram
sns.distplot(df_train['SalePrice'])
# Plot formatting
#plt.legend(prop=12)
# plt.title('House Sale Price')
# plt.xlabel('Sale Price in $')
# plt.ylabel('Cost')
# plt.show()

# Initial visualzation to detect reltaionships

# scatter plot (between numerical vars)
var = 'GrLivArea'
# Method 1: use the pandas dataframe to invoke the visualization call
df_train.plot.scatter(x=var, y='SalePrice')
#plt.show()
# Method 2: use the pandas dataframe to invoke the visualization call
# create a subset of variables to plot
df1 = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
df1.plot.scatter(x=var, y='SalePrice')
#plt.show()

# Bar plot for categorical vars only
var = 'Electrical'
df_train.plot.box(x=var, y='SalePrice')
plt.show()