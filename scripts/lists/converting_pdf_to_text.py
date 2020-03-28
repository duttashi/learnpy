# Motivation: To understand lista and its operations.
# Objective: Read a pdf file containing text into a list. Clean the list data by removing stop words, punctuation etc
# To convert pdf to text format, you will need the `tika` library. Install it as, `pip install tika`

from tika import parser

# Parse data to file
file_data = parser.from_file('../../data/alice.pdf')
# Get file text content
text_data = file_data['content']
print("Pdf converted to text format")
# Open new data file
f = open("../../data/alice.txt", "w")
f.write(str(text_data))      # str() converts to string
print(" Text file now written to disc")
f.close()