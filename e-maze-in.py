m=input().upper()
l=list(m)
x=0
y=0
for ele in l:
    if(ele=='D'):
        x=x-1
    elif(ele=="R"):
        x+=1
    elif(ele=="U"):
        y+=1
    else:
        y-=1
print(x,y)
