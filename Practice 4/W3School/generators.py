mytuple = ("яблоко", "банан", "вишня")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "банан"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("яблоко", "банан", "вишня")

for x in mytuple:
  печать(x)

  mystr = "банан"

for x in mystr:
  печать(x)

  class MyNumbers:
  def __iter__(self):
self.a = 1
    return self

  def __next__(self):
    x = self.a
self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

  class MyNumbers:
  def __iter__(self):
self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)