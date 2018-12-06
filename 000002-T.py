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
