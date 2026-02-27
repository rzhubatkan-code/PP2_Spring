def integer(n): 
    for i in range(n+1):
        if i %12==0:
            yield i 

n = int(input())
value=list(integer(n))
print(value)