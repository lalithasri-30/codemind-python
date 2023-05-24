def reverse(n):
    s=0
    while n!=0:
        i = n%10
        s=s*10+i
        n=n//10
    return s
n=int(input())
if n>0:
    print(reverse(n))
else:
    n=n*-1
    print(-1*reverse(n))