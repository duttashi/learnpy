# create a function which accepts a list and return the multiple of each list item

def multiply_list_items(some_list):
    tot = 0
    for item in some_list:
        tot = item*item
        print(tot)
    return

# create a list
mylist = [4,10,200,3,5]
new_list= multiply_list_items(mylist)
print(new_list)
# create a new list that has elements less than 10 from the above list
another_list = []
for item in new_list:
    if(item<11):
        #another_list = item
        print("Items less than 10 are: ",item)