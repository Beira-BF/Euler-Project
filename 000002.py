a=1
b=2
x=[1]
y=[2]
z=[1,2]
while a<4000000:
    c=a+b
    print(c)
    d=b+c
    print(d)
    if c<4000000:
        x.append(c)
        z.append(c)
    if d<4000000:
        y.append(d)
        z.append(d)
    a=c
    b=d
print(a,x,y,z)

m=sum(x)
n=sum(y)
print(m,n)

l=[]
for i in z:
    if i%2==0:
        l.append(i)

print(l)
o=sum(l)
print(o)
