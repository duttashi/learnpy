# objective: Read a text file, and count the frequency of words

# load required libraries
import os, re, string, collections
from nltk.corpus import stopwords # to filter out words such as: “the“, “a“, and “is“.
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))

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
print("Text data length:",len(txtData))

# do basic text cleaning
# word tokenization
txtData_words = word_tokenize(str(txtData))
## split the words in list
txtData_words = re.split(r'\W+', str(txtData))
# lower case all words in list
txtData_words_lower = [word.lower() for word in txtData_words]
# remove punctuation from words in list
txtData_words_lower_clean = [''.join(c for c in s if c not in string.punctuation) for s in txtData_words_lower]
# remove all stop-words
txtData_clean = [w for w in txtData_words_lower_clean if not w in stop_words]
# count the frequency of word occurence
txtData_clean_words = [word for line in txtData_clean for word in line.split()]
word_frequency_counter = collections.Counter(txtData_clean_words)
print(word_frequency_counter)

# determine unique words in the text data
#txtData_set = set(txtData_clean)
#print(txtData_set)


# close file connection
txtFile.close()

