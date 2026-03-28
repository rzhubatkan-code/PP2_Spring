import re 
s = input().strip()
p = input().strip()
r = input().strip()
result = re.sub(re.escape(p)  , r , s ) 
print(result)