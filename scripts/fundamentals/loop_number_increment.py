# the given program accepts a number and prints consenctive numbers on same line
print("Enter a number: ")
n = int(input())
for i in range(n):
    print(i+1, end="")
for i in range(1,n):
    if(i%2==0):
        print(n, 'equals', x, '*', n // x)
    break
else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')