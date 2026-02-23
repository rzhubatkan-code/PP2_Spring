import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) #   '{ "name":"John", "age":30, "city":"New York"}'

 # You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

import json

print(json.dumps({"name": "John", "age": 30})) {"name": "John", "age": 30} {"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"])) # ["apple", "bananas"]
print(json.dumps(("apple", "bananas"))) # ["apple", "bananas"]
print(json.dumps("hello")) #"hello"
print(json.dumps(42)) # 42
print(json.dumps(31.76)) #31.76
print(json.dumps(True)) # true
print(json.dumps(False)) #false
print(json.dumps(None)) #null

dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null 

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))

