n = int(input())
a = list(map(int,input().split())) 
max_val = max(a)
min_val= min(a) 
for i in range(n) : 
     if a[i] == max_val:
       a[i] = min_val 
for x in a: 
    print(x, end=" ") 
