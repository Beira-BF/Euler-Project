# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a=[]
for i in range(1,60):
    for j in range(1,60):
        if(i*(i+j)==500):
            a.append((i**4-j**4)*(2*i*j))
            print((i**4-j**4)*(2*i*j))
print(a)
print(max(a))