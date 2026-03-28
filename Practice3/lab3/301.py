def check(n) : 
    if n == 0 : 
        return "Valid"
    while n > 0:
        digit = n%10 
        if digit % 2 != 0: 
            return "Not valid"
        n = n// 10 
    return "Valid" 

x = int(input()) 
result=check(x)
print(result) 