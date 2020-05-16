n,x=list(map(int,input().split()))
ls=list(map(int,input().split()))
for i in range(0,x):
    p,y,z=list(map(int,input().split()))
    while(p==1):
        ls[y]=z
        break;
    else:
        print(sum(ls[y:z+1]))

