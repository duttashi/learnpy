# Motivation: To understand list and its operations.
# Objective: Read a text data file into a list. Clean the list data by removing stop words, punctuation etc
# reference: https://cbrownley.wordpress.com/2016/06/26/parsing-pdfs-in-python-with-tika/

# load required libraries
import re
from nltk.corpus import stopwords # to filter out words such as: “the“, “a“, and “is“.
from nltk.stem.porter import PorterStemmer # stemming of words
porter = PorterStemmer()
stop_words = set(stopwords.words('english'))

# read the text file from disc into a list
with(open("../../data/imbalanced.txt",encoding="utf-8")) as f:
    text_content = [line.rstrip() for line in f]

# initialize an empty list and populate it with data read from file
word_lists = []
without_empty_strings = []

word_lists = re.split(r'\W', str(text_content))
# print(word_lists)

# clean data function
def clean_data(textfile):
    words = re.split(r'\W+', str(textfile))
    lower_case_words = [word.lower() for word in words]
    for string in lower_case_words:
        if (string != ""):
            without_empty_strings.append(string)
    words = [w for w in without_empty_strings if not w in stop_words]
    stemmed = [porter.stem(word) for word in words]
    sorted_words = words.sort()
    print("\n The words are: ", without_empty_strings)
    print("\n First 100 Stem words are: ", stemmed[:100])
    print("\n First 100 sorted words are: ", sorted_words)
    return 0
# invoke the function
print(clean_data(word_lists))


# define a function to count the average word length
def avg_word_length(sentence):
    words = re.split(r'\W+', str(sentence))
    return (sum(len(word) for word in words)/len(words))
avg_word_len = avg_word_length(word_lists)
print("The average word length is: ", avg_word_len)

# define a function to lowercase all words
# def words_to_lower(sentence):
#     words = re.split(r'\W+', str(sentence))
#     lower_case_words = [word.lower() for word in words]
#     return lower_case_words
# # call the lower case function
# words_lower = words_to_lower(word_lists)
# print("\n Words in lower case are: ", words_lower)
# #print("\n Data type: ", type(words_lower))
# print(words_lower)

# define a function to sort the lower cased words
# def sort_words(sentence):
#     words = re.split(r'\W+', str(sentence))
#     lower_case_words = [word.lower() for word in words]
#     sorted_words = lower_case_words.sort()
#     print("\n Sorted Words ", sorted_words)
#     return sorted_words


