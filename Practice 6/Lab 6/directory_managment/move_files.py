import os 
import shutil

extension = ".txt" 
txt_files = []

for file in os.listdir("."):
    if file.endswith(extension):
        txt_files.append(file)

if len(txt_files) > 0:
    file_move = txt_files[0]
    folder = "PP2\Practice 6\Lab 6"
    result = os.path.join(folder , file_move)
    shutil.move(file_move , result) 
else:
    print("Files did not find") 

