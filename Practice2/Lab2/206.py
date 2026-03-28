n = int(input()) 
numbers = list(map(int, input().split()))
result= -99999999999
for i in numbers:
     if result < i:
        result = i 
print(result)

