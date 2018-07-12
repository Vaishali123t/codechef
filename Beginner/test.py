t=int(input())
for w in range(t):
    n,a,b=map(int,input().split())
    x=list(input().split())
    y=list(map(int,input().split()))
    print(x)
    print(y)
    c=0
    d=0
    for j in range(n):
        if(x[j]=='1'):
            c+=1
            print('hello')
        if(x[j]=='1'):
            d+=1
            print('hello')
    k=c/n*d/n
    print(k) 
