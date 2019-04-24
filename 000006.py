# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
a=[]
b=[]
for i in range (1,101):
    a.append(i*i)
    b.append(i)
print(a,b)
c=sum(a)
print(c)
d=sum(b)
print(d)
e=d*d
print(e)
print(abs(e-c))