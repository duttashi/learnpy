# Objective: create a list and convert it to a pandas data frame
# script create date: 23/Feb/2020

# load library
import pandas as pd

# creat a dictionary
mydict = {'name':'ashish',
          'age':28,
          'salary':20000
          }
mydict

# Method #1: Create multiple lists.
# Append/add new items to a dictionary
name_list = ['ashish','alex','bob']
age_list = [15,29,37]
salary_list = [10000,2987,3456]
# Convert multiple lists into a dictionary object
mydict = {'name':[],'age':[],'salary':[]}
mydict['name'].append(name_list)
mydict['age'].append(age_list)
mydict['salary'].append(salary_list)

# convert dictionary to pandas dataframe
df= pd.DataFrame(mydict)
print("\n Method # 1")
print(df)

# Method #2: Simple and elegant
# Create a data frame and within it create a dictionary. Within the dictionary, create key name as column name
# and put (multiple key values as a list
df = pd.DataFrame(data={'name':['ashish','alex','sandy'],
                        'age':[18,23,34],
                        'salary':[1876,2786,3478]
                        }
                  )
print("\n Method # 2")
print(df)

# Method #3: Create dataframe using existing list objects
df = pd.DataFrame(data={'name': name_list,
                        'age': age_list,
                        'salary': salary_list
                        }
                  )
print("\n Method # 3")
print(df)

