#python3
t=int(input())
for i in range(t):
    s=input()
    count=0
    for j in range(len(s)-3):
        c=0
        h=0
        e=0
        f=0
        if s[j]=='c' or s[j+1]=='c' or s[j+2]=='c' or s[j+3]=='c':
            c+=1
        if s[j]=='h' or s[j+1]=='h' or s[j+2]=='h' or s[j+3]=='h':
            h+=1
        if s[j]=='e' or s[j+1]=='e' or s[j+2]=='e' or s[j+3]=='e':
            e+=1
        if s[j]=='f' or s[j+1]=='f' or s[j+2]=='f' or s[j+3]=='f':
            f+=1
        if c==h==e==f==1:
            count+=1
    if count!=0:
        print('lovely '+str(count))
    else:
        print('normal')
            
        
