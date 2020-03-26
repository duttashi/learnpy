# the given program accepts a number and prints the prime number
print("Enter a number: ")
n = int(input())
for n in range(2,n):
    if(n % 2==0):
        print(n)
    #break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')