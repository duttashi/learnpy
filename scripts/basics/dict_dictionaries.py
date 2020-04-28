# Dictionaries

d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key, d[key])

# shallow copy
m = {**d}
print(m)

# modifying a dictionary
d['e']=10
for key in d:
    print(key, d[key])