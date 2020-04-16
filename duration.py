n=int(input())
for i in range(0,n):
    sh,sm,eh,em=input().split()
    h=abs(int(eh)-int(sh))
    m=(int(em)-int(sm))
    if(m<0):
        h=h-1
        m=m+60
        print(h,abs(m))
    else:
        print(h,abs(m))
