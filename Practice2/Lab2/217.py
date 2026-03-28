import sys
input_data=sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    phone_numbers=input_data[1:n+1]
counts={}
for phone in phone_numbers:
    counts[phone]=counts.get(phone, 0) +1 
result=0 
for x in counts.values():
    if x ==3 :
         result +=1 
print(result)

























