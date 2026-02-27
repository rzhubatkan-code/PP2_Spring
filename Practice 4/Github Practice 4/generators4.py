def square(a , b): 
    for i in range(a , b): 
        yield i ** 2

x = int(input()) 
y = int(input()) 
result = list(square(x , y)) 
print(result)