import os
import shutil

file = "file1.txt"

with open(file , "a") as f: # Append new line
    f.write("\nThe new line") 

with open(file , "r") as f: # Check new line
    print(f.read()) 

backup = "file1_backup.txt" # Copy 
shutil.copy(filename , backup)

delete = "file1_backup.txt" 

if os.path.exists(delete): # Delete file safely
    os.remove(delete) 
else:
    print("File is not have")

