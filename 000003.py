#a=13195
a=600851475143
d=[]
#for i in range(a,1,-1):
#    if a%i==0:
#        c.append(i)
    #print(i)

#print(c)
#d=[]
#for i in range(0,len(c)):
 #   j=2
  #  while j<c[i]:
   #     if c[i]%j==0:
    #        #print(c[i],"not the prime number.")
     #       break
      #  j=j+1
#    else:
#        d.append(c[i])
#print(d)

b=2
while a>=b:
    k=a%b
    if k==0:
        d.append(b)
        a=a/b
    else:
        b=b+1
print(d)



dx=d[0]
for i in range(0,len(d)):
    if dx<d[i]:
        dx=d[i]
print("The largest prime factor is",dx)
