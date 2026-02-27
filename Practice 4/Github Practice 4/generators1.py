
def squartes(n):
    for i in range(n+1):
        yield i **2

n = int(input())
gen = squartes(n)
for square in gen: 
    print(square)

    

