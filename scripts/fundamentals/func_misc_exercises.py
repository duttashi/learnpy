
# Problem 1: What will be the output of the following code
x = 1
def f():
    return x
print (x) # Ans-1
print (f()) # Ans-1

#Problem 2: What will be the output of the following program?
x = 1
def f():
    x = 2
    return x
print (x) # Ans-1
print (f()) # Ans-2
print (x) # Ans-1

#Problem 3: What will be the output of the following program?
x = 1
def f():
        #y = x # UnboundLocalError: local variable 'x' referenced before assignment
        x = 2
        y=1
        return x + y
print (x) # Ans-1
print (f()) # Ans-3
print (x) # Ans-1

# What will be the output of the following program?
x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print (x, y) # 2, 9

#Functions can be called with keyword arguments.
def difference(x, y):
    return x - y
difference(5, 2)

# There is another way of creating functions, using the lambda operator.
cube = lambda x: x ** 3
print(cube(2))

# Write a function count_digits to find number of digits in the given number.
#find_length = lambda dig: len(dig)
def find_num_len(x):
    num_len = len(str(x))
    return num_len
print("Number length is: ",find_num_len(123567890))
