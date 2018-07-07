#python3
t=int(input())
for i in range(t):
    n=int(input())
    a = list(map(int,input().split(' ')))
    l=[]
    for j in range(len(a)):
        for k in range(j+1,len(a)):
            l.append(a[j]+a[k])
    m=max(l)
    c=0
    for k in range(len(l)):
        if l[k]==m:
            c+=1
    p=c/len(l)
    print('%0.8f'%p)
