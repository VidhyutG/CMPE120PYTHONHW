# calculator() function definition
def calculator(number1,number2,operator):
 '''Function accepts 2 numbers and an operator , based on the operator given it will perform the arithmetic operation'''
# if operator is "+",then perform addition and print result
 if operator=="+":
  print(number1+number2)
# else if operator is "-",then perform subtraction and print result
 elif operator=="-":
  print(number1-number2)
# else if operator is "*",then perform multiplication and print result
 elif operator=="*":
  print(number1*number2)
# else if operator is "/",then perform division and print result
 elif operator=="/" and number2!=0:
  print(number1/number2) 
# else if operator is "//",then perform integer division and print result
 elif operator=="//" and number2!=0:
  print(number1//number2)
# else if operator is "**",then perform power operation and print result
 elif operator=="**":
  print(number1**number2)
# else return False
 else:
  return False

def parse_input():
 ''' Converts users string input into a list and assigns each element in the list to the variables to be passed to the calculator function'''
 a = input("Enter equation: ")
 #parses user input into b as a string of characters
 b = list(a)
 #assigns each element in the list to the parameters needed for the calculation
 number1 = b[0]
 operator = b[1]
 number2 = b[2]
 #calls calculator function and parses parameters as needed 
 calculator(int(number1),int(number2),operator)

