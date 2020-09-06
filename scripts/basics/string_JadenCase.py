# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 09:15:46 2020
# Source: https://www.codewars.com/kata/5390bac347d09b7da40006f6
@author: Ashish
"""

def to_jaden_case(string):
    string = string.lower()
    words = string.split(' ')
    
    capitalized_words = []
    for word in words:
        title_case_word = word[0].upper() + word[1:]
        capitalized_words.append(title_case_word)
        output = ' '.join(capitalized_words)
    return output

str = "How Can Mirrors Be Real If Our Eyes Aren'T Real"
print(to_jaden_case(str))