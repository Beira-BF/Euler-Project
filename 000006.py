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