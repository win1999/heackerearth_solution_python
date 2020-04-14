n=int(input())
for i in range(0,n):
    s,s1=input().split()
    lst=list(s)
    lst1=list(s1)
    lst.sort()
    lst1.sort()
    if(lst==lst1):
        print("YES")
    else:
        print("NO")
