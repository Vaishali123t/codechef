#python3
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    dicts=list(input().split())
    r=[]
    for j in range(k):
        a=input().split()
        r=r+a
    for j in dicts:
        if j in r:
            print('YES',end=' ')
        else:
            print('NO',end=' ')
    
