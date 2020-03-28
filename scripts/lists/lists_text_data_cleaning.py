# Motivation: To understand list and its operations.
# Objective: Read a text data file into a list. Clean the list data by removing stop words, punctuation etc

# read the text file from disc into a list
with(open("'../../data/alice.txt'")) as f:
    text_content = [line.rstrip() for line in f]
print(text_content)



