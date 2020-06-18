t=int(input())

for _ in range(t):
    green,purpule=map(int,input().split())
    solve=int(input())
    count=0
    count1=0
    for _ in range(solve):
        s,d=map(int,input().split())
        count+=s
        count1+=d
        z=count*purpule+count1*green
        m=count*green+count1*purpule
    print(min(z,m))
