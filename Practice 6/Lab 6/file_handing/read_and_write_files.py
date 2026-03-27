import os 
with open("file1.txt" , "w") as f:
    f.write("Hello World !\nHello Python ! ")

with open("file2.txt" , "w") as f:
    f.write("first line \n second line \n third line")
with open("file3.txt" , "w") as f:
    f.write("Hello Kbtu\nHello World\nHello Python\nHello Ruslan")

with open("file1.txt" , "r") as f: # First way
    print(f.read())

with open("file2.txt" , "r") as f: # Second way
    for line in f:
        print(line.strip())

with open("file3.txt" , "r") as f: # Third way
    lines= f.readlines()
    print(lines) 
