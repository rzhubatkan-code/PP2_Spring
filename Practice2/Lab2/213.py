n = int(input()) 
if n < 2:
    print("No") 
else:
    prime=True
    for i in range(2 , int(n**0.5) +1 ):
        if n % i == 0:
            prime=False 
            break 
if prime :
    print("Yes") 
else: 
    print("No") 