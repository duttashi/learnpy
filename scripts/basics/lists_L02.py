#import this
# make two empty lists
lower = []; upper = [];
# set a midpoint
midpoint = 5;
# split the numbers into lower and upper
for i in range(10):
    if (i < midpoint):
        lower.append(i)
    else:
        upper.append(i)
print(lower, "----", upper)
# list indexing
print(lower[0:3])

