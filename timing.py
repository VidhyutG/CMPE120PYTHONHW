import time

def calculate_time(func):
 '''decorator fuction to calculate time taken to run a functio'''
 def innermethod():
  '''inner function of decorator to incorporate changes to the function passed'''
  begin = time.time()
  timer()
  end = time.time()
  print("Total time",end-begin)
 return innermethod
#defining function to be called within decorator
def timer():
  time.sleep(1)
  
myfunction = calculate_time(timer)
#calls function to time
myfunction()
