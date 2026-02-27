def decrease(n) : 
    for i in range(n+1):
       yield i 

n = int(input()) 
result=list(decrease(n))
result.reverse()
print(result)