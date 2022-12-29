#calculator program

from replit import clear
def calculator():
  """ Recursive function to reset everthing"""
  
  def add(n1,n2):
    """ To add two numbers """
    return n1+n2
  
  def subtract(n1,n2):
    """ To subtract two numbers """
    return n1-n2
    
  def multiply(n1,n2):
    """ To multiply two numbers"""
    return n1*n2
  
  def divide(n1,n2):
    """ To divide two numbers """
    return n1/n2
  
  operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide,
  }
  from art import logo
  print(logo)
  n1 = float(input("Enter first number : "))
  n2 = float(input("Enter second number : "))
  
  should_continue=True
  while should_continue:
    
    for symbol in operations:
      print(symbol)
      
    operation_symbol = input("Pick a operation symbol from above line : ")
    calculation_function = operations[operation_symbol]
    answer= calculation_function(n1,n2)
    print(f"{n1} {operation_symbol} {n2} = {answer} ")
  
    should_continue = input("To continue calculating press 'y' and press 'n' to clear screen : ")
  
    if should_continue == "n":
      should_continue=False
      clear()
      calculator()
    if should_continue == "y":
      new_n = float(input("Enter a number : "))
      n1=answer
      n2=new_n

calculator()
  
