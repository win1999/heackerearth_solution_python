def multiplyList(myList) : 
      
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = (result * x)% 1000000007  
    return result  

n=int(input())
list1=list(map(int,input().split())) 
print(multiplyList(list1)) 
