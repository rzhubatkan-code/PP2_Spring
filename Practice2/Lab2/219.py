import sys 
input_data=sys.stdin.read().split()
if input_data:
    n=int(input_data[0])
    doramas={}
    current=1
    for _ in range(n):
        name= input_data[current]
        episodes=int(input_data[current+1])
        doramas[name]=doramas.get(name, 0 ) + episodes
        current +=2 
sorted_names=sorted(doramas.keys()) 
for name in sorted_names:
    print(f"{name} {doramas[name]}")