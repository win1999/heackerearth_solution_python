s=input()
score=0
for j in range(len(s)): 
    score += (ord(s[j])- ord('a') + 1) 
print(score)
