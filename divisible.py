x=int(input())

data = [int(x) for x in input().split()]
lis=[]
n=int(x/2)
for i in data[0:n]:
    last=(repr(i)[0])
    lis.append(last)
for i in data[n:]:
    last=(repr(i)[-1])
    lis.append(last)
z="".join(lis)
if(int(z)%11==0):
    print("OUI")
else:print("NON")

     
    
