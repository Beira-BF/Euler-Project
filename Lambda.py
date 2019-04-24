li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
li=sorted(li, key=lambda x:x["age"])
print(li)
from functools import reduce

#reduce 必须要迭代
a=[5,6,7,8]
b=8
li=reduce(lambda a,b: a+b,a,b)
print(li)


print(reduce(lambda x,y: x + y, range(1,1+int(input(">")))))

