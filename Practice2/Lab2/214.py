n = int(input()) 
a = list(map(int, input().split())) 
most=a[0]
max_count=0 

for x in sorted(set(a)): 
    current_count=a.count(x)
    if current_count>max_count:
        max_count=current_count
        most = x 
print(most)