import os 

path = "PP2\Practice 6\Lab 6" 

os.makedirs(path , exist_ok = True)  # Create nested directories

items = os.listdir(".") 
for item in items:
    print(item) 
