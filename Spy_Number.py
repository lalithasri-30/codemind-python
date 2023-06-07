n=int(input())
a=0
m=1
while n!=0:
    i=n%10
    n=n//10
    a+=i
    m*=i
if a==m:
    print("Spy Number")
else:
    print("Not Spy Number")