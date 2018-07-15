t=int(input())
ans=[]
for i in range(t):
	l,k=map(int,input().split())	
	ans.append("Case "+str(i+1)+": "+str(sum(x for x in range(l-k+2))))
for i in ans:
	print(i)
