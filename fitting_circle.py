x=int(input())
for i in range(0,x):
    a,b=list(map(int,input().split()))
    if(a>b):
        print(int(a/b))
    else:
        print(int(b/a))
