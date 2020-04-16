c=int(input())
for i in range(0,c):
    n=int(input())
    n=n+2*(6-(n-1)%12)-1
    if(n%2<2):
        print(n,"WS")
    elif(n%6==2 or n%6==5):
        print(n,"MS")
    else:
        printf(n,"AS")
