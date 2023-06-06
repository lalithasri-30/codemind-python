import math

n = int(input())
c = 0
sqr = n * n
temp = n

while temp > 0:
    c += 1
    temp = temp // 10

flag = math.floor(pow(10, c))
last = sqr % flag

if last == n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
