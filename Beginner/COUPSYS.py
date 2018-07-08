#python3
t=int(input())

for i in range(t):
    d1=0
    d2=0
    d3=0
    c1=0
    c2=0
    c3=0
    
    n=int(input())
    for j in range(n):
        c,l,d=map(int,input().split())
        if l==1:
            if d>d1:
                d1=d
                c1=c
            elif d==d1 and c1>c:
                c1=c
        elif l==2:
            if d>d2:
                d2=d
                c2=c
            elif d==d2 and c2>c:
                c2=c
        else:
            if d>d3:
                d3=d
                c3=c
            elif d==d3 and c3>c:
                c3=c

    print(d1,c1)
    print(d2,c2)
    print(d3,c3)
    
            
        
        
   
    
    
        
        
    
