#python3
t=int(input())
for i in range(t):
    a=0
    b=0
    n,A,B=map(int,input().split())
    ar=list(map(int,input().split()))
    for j in range(n):
        if A==ar[j]:
            a+=1
        if B==ar[j]:
            b+=1
    p=a/n*b/n
    print("%0.10f"%p)
            
