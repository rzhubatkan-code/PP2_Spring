def sqrt(a , b):
    for i in range(a, b+1): 
        yield i * i 
a , b = list(map(int , input().split())) 
for x in sqrt(a,b):
    print(x) 
    