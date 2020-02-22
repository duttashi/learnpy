# Objective: create a global list and pass it to a function. Inside the function pop an item then append an item to list.
# Then return the new list

mylist = [1,2,3,4,'apple',12.34]
print(mylist)

def somelist():
    newlist = mylist
    newlist.pop()
    newlist.append("god is great")
    return newlist

print(somelist())
