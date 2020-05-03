list_in = input().split(" ")
number = list(list_in[0])
changes = int(list_in[1])
i = 0
 
while i < changes:
    if number[i] != '9':
        number[i] = '9'
    else:
        changes += 1
    i += 1
    
 
print("".join(number))
