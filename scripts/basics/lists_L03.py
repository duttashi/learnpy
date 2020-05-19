# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:48:09 2020

@author: Ashish
"""
# prompt for a number and create a list using the number
# show the list and ask for a number to be removed
# remove the number and show the new list

# prompt for a number from user
varnum = int(input("Enter a number: "))
nums_list = list(range(1, varnum+1))
print(nums_list)
# prompt for a number to be removed from the above list
print("List Operations")

remove_num = int(input("Which number you want to remove from list: "))
# get the indices
item_pos = [i for i in range(len(nums_list)) if nums_list[i] == remove_num]
print("number position", item_pos)
item_pop_val = nums_list.pop(remove_num)
print("removed number value: ", item_pop_val," remove num list position", item_pos)
# now square the popped number and insert it back into its position in list
num_square = item_pop_val*item_pop_val
print(num_square)

# get the indices
item_pos = [i for i in range(len(nums_list)) if nums_list[i] == remove_num]
# print("The item position for number: ", x, "in number list is: ", item_pos)
# nums_list.insert(item_pos, num_square)
nums_list[item_pos:item_pos] = num_square
print("Revised list is: ", nums_list)
