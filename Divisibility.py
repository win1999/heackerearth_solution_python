x=int(input())

data = [int(x) for x in input().split()]
lis=[]
for i in (data):
    y=(repr(i)[-1])
    lis.append(y)
d="".join(lis) 
if(int(d)%10==0):
    print("Yes")
else:print("No")
    
