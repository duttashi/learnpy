# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:36:49 2020
Titanic case study
Data source: https://www.kaggle.com/c/titanic/data
@author: Ashish
"""

# load the required libraries
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier

print(os.getcwd())
# read the data in memory
df_train = pd.read_csv('../../data/titanic_train.csv', keep_default_na= True)
df_test = pd.read_csv('../../data/titanic_test.csv', keep_default_na= True)

# replace the missing values coded as na with NAN
# print column name and dat types
print(df_train.info())
print("\n------------")
print(df_test.info())

# Change to categorical
# df_train['Survived'] = df_train['Survived'].apply(str)
# df_train['Pclass'] = df_train['Pclass'].apply(str)
# df_train['Sex'] = df_train['Sex'].apply(str)
# df_train['Embarked'] = df_train['Embarked'].apply(str)

# df_test['Pclass'] = df_test['Pclass'].apply(str)
# df_test['Sex'] = df_test['Sex'].apply(str)
# df_test['Embarked'] = df_test['Embarked'].apply(str)

print(df_train.info()) 

y = df_train["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(df_train[features])
X_test = pd.get_dummies(df_test[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': df_test.PassengerId, 'Survived': predictions})
output.to_csv('../../data/titanic_my_submission.csv', index=False)
print("Your submission was successfully saved!")

import matplotlib.pyplot as plt
import seaborn as sns

#Using Pearson Correlation
plt.figure(figsize=(12,10))
# print(df_train.info())
cor = df_train.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()
# print(cor)
#Correlation with output variable
cor_target = abs(cor["Survived"])
#Selecting highly correlated features
relevant_features = cor_target[cor_target>0.3]
print(relevant_features)