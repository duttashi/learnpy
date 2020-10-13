# Motivation: To understand list and its operations.
# Objective: Read a pdf file and convert it to text format. Then write this file to disc
# Reference: The solution to use tika package was found in this SO post https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file
# To convert pdf to text format, you will need the `tika` library. Install it as, `pip install tika`

from tika import parser

# Parse data to file
file_data = parser.from_file('../../data/imbalanced.pdf')
# Get file text content
text_data = file_data['content']
print("Pdf converted to text format")
# Open new data file
# if there is an error like, "UnicodeEncodeError: 'charmap' codec can't encode character '\ufffd' in position 6029: character maps to <undefined>"
# then add, `encoding="utf-8"` to the open() as shown below
f = open("../../data/imbalanced.txt", "w",encoding="utf-8")
f.write(str(text_data))      # str() converts to string
print(" Text file now written to disc")
f.close()