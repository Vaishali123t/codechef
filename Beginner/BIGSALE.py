#python3
t=int(input())
for i in range(t):
    n=int(input())
    org=0
    total=0
    for j in range(n):
        p,q,d=map(int,input().split())
        org+=p*q
        new=(q+q*d/100)
        dis=new*d/100
        sp=new-dis
        total+=p*sp
    diff=org-total
    print('%0.9f'%diff)
        
        
