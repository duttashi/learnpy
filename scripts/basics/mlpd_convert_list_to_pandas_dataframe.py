# Objective: create a list and convert it to a pandas data frame
# script create date: 23/Feb/2020

# load library
import pandas as pd
# creat a list
mylist = [46,'ashish',10000]
# convert list to pandas dataframe
df= pd.DataFrame(mylist)

# show the data type of dataframe. Use info(). Equivalent in R is str()
# See this SO post: https://stackoverflow.com/questions/27637281/what-are-python-pandas-equivalents-for-r-functions-like-str-summary-and-he
df.info()
df.memory_usage()
print("Dataframe objects are: ",df.head())

# As we can see the data frame has no column headers. So add them using columns() function.
# But first transpose the list items from column to rows
df = pd.DataFrame(mylist).T
#print(df)
# Now add column headers to the coerced list
df.columns = ['age', 'name', 'salary']
print(df)


