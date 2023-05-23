n=int(input())
lens=list(map(int,input().split()))
#finding max comm divisor(GCD) of al divisor
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
mxlen=lens[0]
for i in range(1,n):
    mxlen=gcd(mxlen,lens[i])
print(mxlen)