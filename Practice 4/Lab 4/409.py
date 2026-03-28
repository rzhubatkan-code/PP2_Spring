def two(n):
    for i in range(n+1):
        yield 2 ** i

n = int(input()) 
for i in two(n):
    print(  i , end=" ")