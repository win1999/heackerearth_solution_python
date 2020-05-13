x=list(map(int,input()))
if(x[-1]==6):
    print("-1")
else:
    y=x.count(6)
    print(len(x)-y)
