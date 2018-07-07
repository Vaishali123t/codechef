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
        dis=new*q/100
        sp=new-dis
        tot=p*sp
        total+=tot
    print(org-total)
        
        
