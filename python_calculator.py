num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Select an Operator: + - * /")
if operator == "+":
  print(num1+num2)
  #print(round(num1+num2))
elif operator == "-":
  print(num1-num2)
elif operator == "/":
  print(num1/num2)
elif operator == "*":
  print(num1*num2)
else:
  print("Error!, Please check the operator and try again")

