#python3
t=int(input())
for i in range(t):
    n=int(input())
    res=list(map(int,input().split()))
    c=sum(res)
    if c%2==0:
        print('NO')
    else:
        print('YES')
