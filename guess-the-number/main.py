# Guess The Number Game: A simple game that allows the user to guess the number
# Built with programming elements using custom functions, while loops, logic statements, constants, and scopes. 

import random

EASY_LEVEL = 10 #more attempts makes it easy
HARD_LEVEL = 5  #less attempts makes it hard
logo = """                                                               
 _____                    _____ _          _____           _           
|   __|_ _ ___ ___ ___   |_   _| |_ ___   |   | |_ _ _____| |_ ___ ___ 
|  |  | | | -_|_ -|_ -|    | | |   | -_|  | | | | | |     | . | -_|  _|
|_____|___|___|___|___|    |_| |_|_|___|  |_|___|___|_|_|_|___|___|_|                                                                        

"""

#Function that sets difficulty level of game
def set_level():
  """Sets the level of difficulty chosen by user"""
  level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if level_choice == 'easy':
    return EASY_LEVEL
  elif level_choice == 'hard':
    return HARD_LEVEL

#Function compares user's guess and the number picked by the computer
def compare_num(guess, answer):
  """Compares the user's guess with the answer"""
  if guess == number:
    print(f"You've won! The answer is {answer}.")
    return  
  elif guess > number:
    print("Too high.")
  elif guess < number:
    print("Too low.")

#Function that loops until user guesses number or has no more attempts
def guess(answer):
  """Prompts user to guess number until there are no more attempts or the guess the number correctly"""
  attempts = set_level()
  guess = 0
  game_over = False

  while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    compare_num(guess, answer)

    attempts -= 1
    if attempts == 0:
      game_over = True
      print("You have no more attempts left. You've lost :(")
    elif guess != answer:
      print("Guess again")
    else:
      return

#Chooses a random number from 1 to 100
number = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"Psst, the answer is {number}")

guess(number)