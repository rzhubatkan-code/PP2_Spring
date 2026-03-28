import math 
def prime(n):
    for num in range(2, n+1):
        isPrime=True 
        for i in range(2 , int(math.sqrt(num) + 1 )):
            if num % i == 0 :
                isPrime= False
                break
        if isPrime:
            yield num

n = int(input()) 
for p in prime(n):
    print(p ,end=" ")