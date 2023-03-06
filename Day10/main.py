from art import logo
from replit import clear
print(logo)

def add(a,b):
  """Add two numbers"""
  return a+b

def subtract(a,b):
  """Subtract two numbers"""
  return a-b

def multiply(a,b):
  """Multiply two numbers"""
  return a*b

def divide(a,b):
  """Divide two numbers"""
  return a/b

operations={
  "+": add, 
  "-": subtract,
  "*": multiply ,
  "/": divide
}
def calculator():
  num1 = float(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)

  flag_continue = True
  while flag_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    answer = operations[operation_symbol](num1,num2)
    print(f"{num1}{operation_symbol}{num2} = {answer}")

    option_continue = input(f"Do you want to continue calculating with {answer} or start over? Type 'y' to continue or 'n' to start over.\n")
    if option_continue == "y":
      num1 = answer
    elif option_continue == "n":
      flag_continue = False
      clear()
      calculator()
    else:
      print("Invalid response")
      flag_continue = False

calculator()

