students = ["Alisher" , "Ruslan" , "Erlik"]
scores = [95 , 82, 90] 
for index , name in enumerate(students , start=1): 
    print(index , name)

result = zip(students , scores)
for name , score in result:
    print(name , score) 



data = ["10", 20, "30", 40]

clean = list(map(int , data)) 
total = sum(clean) 
print(total) 