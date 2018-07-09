#python3
t=int(input())
for i in range(t):
    sq=0
    b=int(input())
    while b/2>1:
        b=b-2
        sq+=int(b/2)
    print(sq)
