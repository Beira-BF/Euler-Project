# Even Fibonacci numbers
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a=[1]*34

a[0] = 1
a[1] = 1

for i in range(2,34):
  a[i]=a[i-1]+a[i-2]
print(a)

sum=0

for i in a:
  if(i%2==0):
    sum=i+sum

print(sum)
