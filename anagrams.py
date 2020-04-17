def makeAnagram(a, b): 
    buffer = [0] * 26
    for char in a: 
        buffer[ord(char) - ord('a')] += 1
    for char in b: 
        buffer[ord(char) - ord('a')] -= 1
    return sum(map(abs, buffer)) 
n=int(input())
for i in range(0,n):
    a=input()
    b=input()
    print(makeAnagram(a,b))
