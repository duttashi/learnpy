# Reference: https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/02%20-%20Lesson.ipynb

import pandas as pd, matplotlib.pyplot as plt
import sys, os, random

# Objective: To make a random list of 1,000 baby names using some specified names we will do the following:
# the initial set of baby names
names = ['Bob','Jessica','Mary','John','Mel']
random.seed(2020)
random_names = [names[random.randint(0,len(names))] for i in range(3)]

# Print first 10 records
print(random_names[:2])
