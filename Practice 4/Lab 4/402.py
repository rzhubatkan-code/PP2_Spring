def even(n): 
    for i in range(0, n+1 , 2): 
        yield i

n = int(input()) 
for even in even(n):
    if even != 0:
        print("," , end="")
    print(even, end="" )



        