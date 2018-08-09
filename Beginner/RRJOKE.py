#python3
t=int(input())
for i in range(t):
    n=int(input())
    
    for j in range(n):
        x,y=map(int,input().split())
        a=0
    for j in range(1,n+1):
        a^=j
    print(a)
