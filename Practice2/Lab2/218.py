import sys 
input_data=sys.stdin.read().split() 
if input_data: 
    n = int(input_data[0])
    strings= input_data[1:n+1] 
    first={}
    for i in range(n): 
        s = strings[i] 
        if s not in first: 
            first[s] = i+1
sorted_keys=sorted(first.keys())
for key in sorted_keys: 
    print(f"{key} {first[key]}")