import re 
x = input() 
result= re.findall(r"\d" , x ) 
print(*result)