#python3
t=int(input())
for i in range(t):
    count=0
    m,n=map(int,input().split())
    s1=m*(n-1)
    s2=n*(m-1)
    p=m*n
    s=s1+s2
    print(s-p+1)
        
