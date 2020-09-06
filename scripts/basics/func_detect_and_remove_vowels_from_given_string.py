# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:52:49 2020

@author: Ashish
"""

astr = "This website is for losers LOL!"
# lowercase the string
astr = astr.lower()
astr_list = list(astr)
vowels = ['a','e','i','o','u']
astr_len = len(astr_list)
print("string length: ", astr_len)
# print(astr_list)
for i in range(astr_len):
    # print(astr_list[i])
    if (vowels[i] in astr_list):
        print(astr_list[i])
        # astr_list[i]=0
    # else:
    #     continue
        
# print(astr_list)        

    