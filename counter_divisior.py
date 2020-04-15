l,r,k=list(map(int, input().split()))
x = len([i for i in range(l,r+1) if (i % k==0)])
print(x)
