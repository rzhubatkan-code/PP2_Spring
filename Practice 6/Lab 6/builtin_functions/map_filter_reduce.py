from functools import reduce 

numbers = [1, 5, 2, 4, 3, 6, 8, 7, 9, 10]  # Map
squares = map(lambda x: x**2 , numbers)
squares_list= list(squares)

print(numbers) 
print(squares_list)

x = filter(lambda x: x > 5 , numbers)
print(x) 
sort=sorted(squares)

sum_numbers = sum(numbers)

print (sum_numbers)
 
result = reduce(lambda x , y: x*y , [1 ,2, 3, 4]
print(result)