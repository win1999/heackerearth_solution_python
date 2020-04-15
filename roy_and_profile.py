l=int(input())
cases=int(input())
for i in range(0,cases):
    w,h=list(map(int,input().split()))
    if w==l and h==l:
        print("ACCEPTED")
    elif w>=l and h>=l and w==h:
        print("ACCEPTED")
    elif w>=l and h>=l:
        print("CROP IT")
    else:
        print("UPLOAD ANOTHER")
