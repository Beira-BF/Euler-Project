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
