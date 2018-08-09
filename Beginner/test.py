T=int(input())
for p in range(T):
    l=input().split()
    N=int(l[0])
    K=int(l[1])
    s=input()
    l=s.split()
    res=[]
    for i in range(N):
        res.append(0)
    for j in range(K):
        k=input()
        h=k.split()
        for z in range(N):
            if(l[z] in h):
                res[z]=1
    for i in res:
        if(i==1):
            print("YES",end=" ")
        else:
            print("NO",end=" ")
    print()
