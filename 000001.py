# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
a=[]
for i in range(0,1000):
    if i%3==0:
        a.append(i)
        i=i+1

print(a)

b=[]
for i in range(0,1000):
    if i%5==0:
        b.append(i)
        i=i+1

print(b)

c=[i for i in a if i in b]

print(c)

for i in a:
    for j in b:
        if i==j:
            a.remove(i)
            i=i+1

print(a)


e=sum(a)
f=sum(b)
g=e+f
print(g)
