#python3
t=int(input())
b=[]
for i in range(t):
    res=0
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(len(a)):
        res=res^(2*a[j])
    print(res)   
