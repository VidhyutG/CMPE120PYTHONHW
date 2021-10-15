def tripler(func):
 def wrapper():
  func()
  func()
  func()
 return wrapper

def myFunction():
  print("hello")
  
myFunction = tripler(myFunction)

myFunction()
