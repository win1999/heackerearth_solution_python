cases=int(input())
for i in range(0,cases):
    n=int(input())
    if(n%2!=0):
        n=3*n+1
        if(n%2==0):
            print("YES")
        else:
            print("NO")
    else:
        print("Yes")
