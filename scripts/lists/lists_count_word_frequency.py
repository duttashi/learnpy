# objective: Read a text file, and count the frequency of words

# load required libraries
import os, re

# set relative path location
dataPath = os.path.dirname(__file__)
relPath = "C:/Users/Ashoo/Documents/PythonPlayground/learnpy/data/alice.txt"
abs_file_path = os.path.join(dataPath, relPath)

# open the text file from relative path
txtFile = open(abs_file_path, 'r')
# Read text file to list
# python's file.readlines() method returns a list of the lines in the file:
txtData = txtFile.readlines()
# read text file and show its length
print("File length:",len(txtData))
# print text data
print(txtData)
# do basic text cleaning




# close file connection
txtFile.close()

