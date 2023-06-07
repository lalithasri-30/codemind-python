n=int(input())
s=0
sqr=n*n
while sqr!=0:
    rem=sqr%10
    s+=rem
    sqr=sqr//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")