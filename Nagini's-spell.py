n,k,v= input().split(" ")
n=int(n)
k=int(k)
s=list(v)
z=int(n)+4

index=[]
count=0


for i in range(k-1,n):
    test=0
    for j in range(k-1):
        if(s[i-j]=='1'):
            test+=1
        else:
            break
    if(test==k-1):
        index.append(i-k+1)
        count+=1
    else:
	    test=0
	    for j in range(k-1):
	        if(s[i-j]=='0'):
	            test+=1
	        else:
	            break
	    if(test==k-1):
	        index.append(i-k+1)
	        count+=1
	    else:
	        continue


for i in range(count):
	s.pop(index[i])
	s.insert(index[i],'1')


y=[]
x=0
for i in range(n):
    if s[i]=='1':
        x+=1
    else:
        y.append(x)
        x=0
print(max(y))
