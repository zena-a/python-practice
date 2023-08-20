# Hangman Game: Allows you to play the classic game of Hangman. Crafted using random module, loops, if...else conditions, and custom functions.

import random, ascii, words, clearscreen

# Function to get user input
def get_user_input():
   return input('Guess a letter: ').lower()

# Function to update the display based on the guessed letter
def update_display(chosen_word, guess, display):
   for position, letter, in enumerate(chosen_word):
      if letter == guess:
         display[position] = letter

# Function to display the game state
def display_game_state(lives, remaining_letters):
   print(ascii.stages[lives])
   print(f'You have {lives} lives left. Remaining letters: {", ".join(remaining_letters)}')
   print(f'\nWord: {" ".join(display)}')

# Variables
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
end_game = False
lives = 6 

# Create holders for the chosen word
display = ['_'] * word_length

# Prints the hangman logo at the start of the game
print(ascii.logo)

# Testing code - comment out after testing
# print(f'Word is: {chosen_word}.')

# Main game loop
while not end_game:
    guess = get_user_input()
    clearscreen.clear()

    # Removes guessed letter from the list
    if guess in words.letters:
       words.letters.remove(guess)
       # Notifies user if the letter was already guessed
       if guess in display:
          print(f'You have already guessed the letter, {guess}.')

    update_display(chosen_word, guess, display)

    # Deducts from player's lives if wrong letter was chosen
    if guess not in chosen_word:
      lives -= 1
      print(f'The letter {guess} is not in the word.')

    display_game_state(lives, words.letters)

    # Prints win or lose message and the chosen word
    if lives == 0:
        end_game = True
        print(f'\nThe word was: {chosen_word}. \nYou lose! :( ')

    if '_' not in display:
      end_game = True
      print(f'\nYou win! :). \nThe word was: {chosen_word}.')