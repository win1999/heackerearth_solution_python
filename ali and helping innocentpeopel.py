s=input()
check=0
l=['A','E','I','O','U','Y']
if((int(s[0])+int(s[1]))%2==1):
    check=1
if((int(s[3])+int(s[4]))%2==1):
    check=1

if((int(s[4])+int(s[5]))%2==1):
    check=1

if((int(s[7])+int(s[8]))%2==1):
    check=1
if(s[2]==l):
    check=1
if(check==0):
    print("valid")
else:
    print("invalid")
