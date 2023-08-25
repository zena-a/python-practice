# Standard Calculator: A program that simulates the standard functions of a calculator.
# Utilizes modularity through custom functions and dictionaries for data structures.

import os, platform

# Function to clear terminal screen
def clear():
  if platform.system() == 'Windows':
    os.system('cls')
  else:
    os.system('clear')

# Functions for basic arithmetic operations
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1/n2

# Calculator function that performs the selected operation on two numbers
def calculator(n1, n2, operation):
  calc_function = operations[operation]
  return calc_function(n1, n2)

# Dictionary that maps operation symbols to their respective functions
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
  }

# Main function to gather input and manage the flow of the program
def main(num1=0):
  if num1 == 0:
    num1 = float(input("The first number: "))
  else:
    print(f"Your first number is: {num1}")

  # Display available operations
  print(", ".join(operations))

  selected_operation = input("Pick an operation: ")
  num2 = float(input("The second number: "))

  # Perfomr the calculation using the selected operation
  answer = calculator(num1, num2, selected_operation)
  print(f"{num1} {selected_operation} {num2} = {answer}")

  # If user continues the result will be used for further calculations
  should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

  if should_continue == "y":
    clear()
    # Recursion: The main function calls itself to continue the calculation
    main(answer) # Pass the updated answer as num1 for the next calculation
  else:
    print("Goodbye!")

# Entry point of the program
if __name__ == "__main__":
  main()