import sys 
input_data=sys.stdin.read().splitlines()
if input_data: 
    n = int(input_data[0]) 
    db={}
    for i in range(1 , n+1): 
        parts= input_data[i].split()
        command=parts[0]

        if command =="set":
            key = parts[1]
            value = parts[2]
            db[key] = value
        elif command == "get":
             key = parts[1]
             if key in db:
                print(db[key]) 
             else:
                print(f"KE: no key {key} found in the document")
