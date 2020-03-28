# Motivation: To understand list and its operations.
# Objective: Read a text data file into a list. Clean the list data by removing stop words, punctuation etc
# reference: https://cbrownley.wordpress.com/2016/06/26/parsing-pdfs-in-python-with-tika/

# load required libraries
import re

# read the text file from disc into a list
with(open("../../data/alice.txt")) as f:
    text_content = [line.rstrip() for line in f]

# initialize an empty list
word_lists = []
word_lists = re.split(r'\W+', str(text_content))
print(word_lists)

# print word on a new line
for word in word_lists:
    print(word)

# define a function to count the average word length
def avg_word_length(sentence):
    words = re.split(r'\W+', str(sentence))
    return (sum(len(word) for word in words)/len(words))
avg_word_len = avg_word_length(word_lists)
print("The average word length is: ", avg_word_len)

# define a function to lowercase all words
def words_to_lower(sentence):
    words = re.split(r'\W+', str(sentence))
    lower_case_words = [word.lower() for word in words]
    return lower_case_words
# call the lower case function
words_lower = words_to_lower(word_lists)
print("\n Words in lower case are: ", words_lower)
