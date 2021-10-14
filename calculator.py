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
 elif operator=="/":
    if(number2==0)
     print("no division by 0")
  print(number1/number2)
# else if operator is "//",then perform integer division and print result
 elif operator=="//":
  print(number1//number2)
# else if operator is "**",then perform power operation and print result
 elif operator=="**":
  print(number1**number2)
# else return False
 else:
  return False

def parse_input():
 number1, operator, number2 = input("enter equation: ").split()
 calculator(int(number1),int(number2),operator)

