n=int(input())
s=0
negitive=False
if n<0:
    negitive=True
    n=abs(n)
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if negitive:
    s=-s
print(s)