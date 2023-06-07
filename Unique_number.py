n=int(input())
a=[0]*100
c=0
flag=1
while n!=0:
    r=n%10
    a[c]=r
    n=n//10
    c+=1
for i in range (c):
    for j in range (i+1,c):
        if a[i]==a[j]:
            flag=0
if flag==1:
    print("Unique Number")
else:
    print("Not Unique Number")