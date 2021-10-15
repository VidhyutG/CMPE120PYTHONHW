import time

def calculate_time(func):
 def innermethod():
  begin = int(time.time)
  timer()
  end = int(time.time)
  total = end - begin
  print("total time taken: ",total)
 return innermethod

def timer():
  time.sleep(2)
  
function_used = calculate_time(timer)

function_used()
