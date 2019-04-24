# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# Please input 1000000
n = int(input(">"))

a = [True]*(n+1)

a[0] = False
a[1] = False

for i in range(2,n):
    if(a[i] == False):
        continue
    j = i*i
    while(j <= n):
        if(j % i == 0):
            a[j] = False
        j += 2

b = []

for i in range(0,n+1):
    if(a[i]):
        b.append(i)

print(b[10000])