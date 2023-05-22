t=int(input())
for tc in range (1,t+1):
    n,a,b,k=map(int,input().split())
    f=n//a#6//2=3 probs
    v=n//b#6//3=2 probs
    com=n//(a*b)#in 3 probs and 2 probs 6prob is commonso mul by 2
    s=(f+v)-(2*com)
    if((s)>=k):
        print("Win")
    else:
        print("Lose")