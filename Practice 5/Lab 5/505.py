import re 
x = input() 
if re.search(r"^[a-zA-Z].*\d$" , x ):
    print("Yes") 
else:
    print("No") 