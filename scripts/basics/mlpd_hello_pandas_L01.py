# Reference: https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb

import pandas as pd, matplotlib.pyplot as plt
import sys, os

print('Python version '+sys.version)
print('Pandas version '+pd.__version__)

# Create data
# The inital set of baby names and birth rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
# To merge these two lists together we will use the zip function.
babyDataSet = list(zip(names, births))
print(babyDataSet)

# create a dataframe
df = pd.DataFrame(data= babyDataSet, columns=['Names', 'Births'])
print(df)
# export the data to a csv file
df.to_csv('baby_births_data.csv', index= False, header= True)

# get data
# df = pd.read_csv('baby_births_data.csv', header= None)
# print(df)

# Create graph
df['Births'].plot()


# Maximum value in the data set
MaxValue = df['Births'].max()

# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0),
                 xycoords=('axes fraction', 'data'), textcoords='offset points')
plt.show()
print("The most popular name")
df[df['Births'] == df['Births'].max()]
#Sorted.head(1) can also be used

