
# Background: For data manipulation in R, the defacto standard is the dplyr library with its verbs like filter, arrange, group_by, mutate, select and summarise
# Objective: To find similar verbs in python for data manipulation

# invoke required libraries
import pandas as pd
# data_url = "https://github.com/duttashi/learnr/blob/master/data/titanic_train_data.csv"
# Note: when reading data files from url, ensure they are in raw format. For instance, if the above data file url is passed to read_csv() then an error is generated.
data_url = "https://raw.githubusercontent.com/duttashi/learnr/master/data/titanic_train_data.csv"
df = pd.read_table(data_url)

# look at the data structure
print(df.info())
# look at data shape
print(df.shape)
# print the data columns
print(df.head())

# filter
#x = df['Survived']==0
#x = df[df.Survived.eq(1)]
x = df.query('Survived==1')
print(x)