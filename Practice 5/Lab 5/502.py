import re 
txt = input()
x = input()
if re.search(x , txt):
    print("Yes") 
else:
    print("No") 