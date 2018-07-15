#python3
t=int(input())
res=[]
for i in range(t):
    s=0
    l,k=map(int,input().split())
    n=l-k+1
    for j in range(1,n+1):
        s+=j
    res.append(s)
for i in range(t):
    print('Case '+str(i+1)+':',res[i])
