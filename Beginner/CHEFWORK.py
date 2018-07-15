#python3
n=int(input())
c=list(map(int,input().split()))
t=list(map(int,input().split()))
m1=100000
m2=100000
m3=100000
for i in range(n):
    if t[i]==1 and c[i]<m1:
        m1=c[i]
    elif t[i]==2 and c[i]<m2:
        m2=c[i]
    elif t[i]==3 and c[i]<m3:
        m3=c[i]    
print(min(m1+m2,m3))
