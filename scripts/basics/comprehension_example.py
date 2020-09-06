# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:55:32 2020

@author: Ashish
"""

paragraph = ['There was a quick brown fox','There was a big brown cat',
             'The world is a big family']
single_word_list =[]

# For method
for sentence in paragraph:
    for word in sentence.split():
        single_word_list.append(word)
        
print(single_word_list)

# Comprehension method
single_word_list = [word for sentence in paragraph 
                    for word in sentence.split()]
print("List comprehension example")
print(single_word_list)
