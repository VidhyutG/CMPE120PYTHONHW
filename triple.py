def tripler(func):
 '''decorator to call any function passed to it 3x'''
 def wrapper():
  ''' inner function of decorator to call implement its changes'''
  func()
  func()
  func()
 return wrapper

def myFunction():
  print("hello")
  
myFunction = tripler(myFunction)
#calling myFunction
myFunction()
