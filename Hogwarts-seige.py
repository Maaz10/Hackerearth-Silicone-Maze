T = int(input())
def wow():
    if N[i]=='1':
        N.pop(i)
        N.insert(i,'0')
    elif N[i] =='0':
        N.pop(i)
        N.insert(i,'1')

for j in range(T):
    N = list(input())
    length = len(N)-1
    Q=int(input())
    for i in range(Q):
        x,y,z=input().split()
        x=int(x)
        y=int(y)
        z=int(z)
        if z==0:
            for i in range(x,y+1):
                wow()
        elif z==1:
            for i in range(length):
                if  i<x or i>y:
                    wow()                    
    str1 = ''.join(N)
    N.clear()
    print(str1)
