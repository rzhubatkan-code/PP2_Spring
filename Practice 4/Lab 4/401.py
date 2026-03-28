def squares(n):
    result = [] 
    for i in range(1 , n+1): 
       result.append(i ** 2) 
    return result 

x = int(input())
for num in squares(x):
    print(num)