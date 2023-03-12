from art import logo

#Add
def add(n1,n2):
  return n1 + n2

#Subtract
def subtract (n1, n2):
  return n1 - n2

#Multiply
def multiply (n1, n2):
  return n1 * n2

#Divide
def divide (n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
import os
def calculator():
  print(logo)
  num1 = float(input("What's the fist number? "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  while  should_continue:
    operation_symbol  = input("Pick an operation from the line above ")
    num2 = float(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    answer1 = calculation_function (num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer1}")
  
    continuation = input(f"Type 'y'  to continue caltulation with {answer1} or 'n' to exit ").lower()
    if continuation == "n":
      should_continue = False
      os.system('clear')
      calculator()
    elif continuation == "y":
      num1 = answer1
    
    

calculator()

           

          