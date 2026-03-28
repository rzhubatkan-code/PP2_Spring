import sys
input_data= sys.stdin.read().split()
if input_data:
    n = int(input_data[0]) 
    surnames = input_data[1:n+1] 
    unique_surnames= set(surnames)
print(len(unique_surnames))