# A hangman game using random module with loops, if...else conditions, and formatted strings.

import random, ascii, words, clearscreen

# Chooses word from word list and calculates length of word
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

# Player has six lives and end of game is set to False
end_game = False
lives = 6 

# Prints the hangman logo at the start of the game
print(ascii.logo)

# Testing code - comment out after testing
print(f'Psst, the solution is {chosen_word}.')

# Create holders for chosen word
display = []
for _ in range(word_length):
    display += '_'

while not end_game:
    guess = input('Guess a letter: ').lower()
    clearscreen.clear()

    if guess in display:
      print(f'You have already guessed the letter, {guess}.')

    for position in range(word_length):
      letter = chosen_word[position]
      # Testing code - comment out after testing
      print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}')

      if letter == guess:
        display[position] = letter

    if guess not in chosen_word:
       lives -= 1
       print(f'The letter {guess} is not in the word.')

       if lives == 0:
          end_game = True
          print('You lose.')

    if '_' not in display:
       end_game = True
       print('You win.')

    print(ascii.stages[lives])

