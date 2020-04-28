# Objective: Create a function and pass a list as argument to it
# Create a list of numbers and strings. Pass this list as argument to a function. Inside the function, add the numbers and return

# create a function
def add_list_items(mylist):
    sum_numbers = 0
    for i in mylist:
        sum_numbers += i
    return sum_numbers

# create a list
some_list = [1,2,3,5]
# invoke function call
result = add_list_items(some_list)
print(result)
