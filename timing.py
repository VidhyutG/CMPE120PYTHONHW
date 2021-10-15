import time

def calculate_time(func):
 def innermethod():
  begin = time.time()
  timer()
  end = time.time()
  print(f'total time taken: {end-begin}')
 return innermethod

def timer():
  time.sleep(2)
  
function_used = calculate_time(timer)

function_used()
