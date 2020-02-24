# objective: Develop an end-to-end case study on the success of ceasarian operations or something like that
# Include, EDA, relationship detection, feature selection & feature engineering, predictive modelling
# script create date: 24/Feb/2020
# Data source: http://archive.ics.uci.edu/ml/datasets/Caesarian+Section+Classification+Dataset
# Missing values: None

# load the required libraries
import pandas as pd, numpy as np, seaborn as sns, matplotlib.pyplot as plt
# read the data in memory
df_train = pd.read_csv('../../data/caesarian.csv', keep_default_na= True)
# print column name and dat types
print(df_train.info()) # 6 variables, 3 are discrete, 1 is integer, 1 is time and 1 is categorical with 2 levels

# Exploratory data analysis

# Data management decisions
# 1. change data type of the 3 discrete variables from integer to categorical
df_train['blood_pressure'] = df_train['blood_pressure'].apply(str)
df_train['heart_problem'] = df_train['heart_problem'].apply(str)
df_train['caesarian'] = df_train['caesarian'].apply(str)
# change value in variable caesarian to something more readable
df_train['blood_pressure'] = df_train['blood_pressure'].map({'0':'low','1':'normal','2':'high'})
df_train['heart_problem'] = df_train['heart_problem'].map({'0':'apt','1':'inept'})
df_train['delivery_time'] = df_train['delivery_time'].map({'0':'timely','1':'premature','3':'latecomer'})
df_train['caesarian'] = df_train['caesarian'].map({'0':'No','1':'Yes'})

print(df_train.info())

# 2. Initial visualization
var = 'caesarian'
sns.countplot(data = df_train, x = var, hue = 'caesarian', palette = ('r', 'b'))
#plt.show()
#scatterplot
sns.set()
cols = ['age', 'delivery_number', 'delivery_time', 'blood_pressure', 'heart_problem', 'caesarian']
sns.pairplot(df_train[cols], height = 2.5)
#plt.show();

# 3. Correlation detection
corrmat = df_train.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);
#plt.show() # delivery_number and age are correlated
# 3. Correlation detection amongst numerical variables. Zoomed heatmap
k = 3 #number of variables for heatmap
cols = corrmat.nlargest(k, 'delivery_number')['delivery_number'].index
cm = np.corrcoef(df_train[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show() # delivery number and age have a low positive correlation. delivery number, delivery time and age have low negative correlation





