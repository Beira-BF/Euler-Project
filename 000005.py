# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
a = [2,3,5,7,11,13,17,19]

b = [-1]*len(a)
#print(b)
j = 0
for i in a:
    m = 20
    while(m != 0):
        m = int(m / i)
        b[j] += 1
    j += 1

m = 1
for i in range(0,len(a)):
    m *= (a[i]**b[i])

print( "The smallest positive number is:",m)