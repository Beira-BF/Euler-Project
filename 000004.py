# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
mul=[]
for i in range(100,999):
    for j in range(i,999):
        mul.append(i*j)

a=[]
for i in mul:
    if(list(str(i)))==list(reversed(list(str(i)))):
        a.append(i)
print(max(a))