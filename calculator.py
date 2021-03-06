# calculator() function definition
def calculator(number1,number2,operator):
 '''Function accepts 2 numbers and an operator , based on the operator given it will perform the arithmetic operation'''
# if operator is "+",then perform addition and print result
 if operator=="+":
  return number1+number2
# else if operator is "-",then perform subtraction and print result
 elif operator=="-":
  return number1-number2
# else if operator is "*",then perform multiplication and print result
 elif operator=="*":
  return number1*number2
# else if operator is "/",then perform division and print result
 elif operator=="/" and number2!=0:
  return number1/number2 
# else if operator is "//",then perform integer division and print result
 elif operator=="//" and number2!=0:
  return number1//number2
# else if operator is "**",then perform power operation and print result
 elif operator=="**":
  return number1**number2
# else return False
 else:
  return False

def parse_input():
 ''' Converts users string input into a list and assigns each element in the list to the variables to be passed to the calculator function'''
 a = input("Enter equation:")
 #parses user input into b as a string of characters
 b = list(a)
 #assigns each element in the list to the parameters needed for the calculation
 c = len(b)
 #based on length of list , it assigns the elements in the list to the parameters to be passed
 #if operator has 1 character
 if c==3:
  number1 = b[0]
  operator = b[1]
  number2 = b[2]
 #if operator requires 2 characters
 elif c==4:
  number1 = b[0]
  operator = b[1]+b[2]
  number2 = b[3]
 #calls calculator function and parses parameters as needed 
 calculator(float(number1),float(number2),operator)
