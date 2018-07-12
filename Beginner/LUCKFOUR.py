#python3
t=int(input())
for i in range(t):
    count=0
    n=input()
    s=list(n)
    l=len(s)
    for j in range(l):
        if s[j]=='4':
            count+=1
    print(count)
        
