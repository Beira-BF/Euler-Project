# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = int(input("Please enter a number:"))

while(n % 2 == 0):
    n /= 2
j = 3
while(n > j):
    if(n % j == 0):
        n = n / j
    else:
        j = j + 2
print(int(n))