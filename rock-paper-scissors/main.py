# A game of rock, paper, scissors using random module, if..else..elif statements
# and while loops

import random, ascii_art
from clearscreen import clear

# Stores ascii art in a list
graphics = [ascii_art.rock, ascii_art.paper, ascii_art.scissors]

def play_again():
	return input('Do you want to play again? (yes/no): ').lower().startswith('y')

# Game loops until player selects no
while True:
	# Clears screen for new round
	clear()
	# Prompts user for option (rock, paper, or scissors)
	player_choice = int(input('Choose your weapon! Type 0 for rock, 1 for paper, or 2 for scissors: '))

	# Print player's choice
	print('You chose: ')
	if player_choice >= 3 or player_choice < 0:
		print('Invalid input! You lose :(')
	else:
		print(graphics[player_choice])

	# Computer's turn. Random value is chosen. Prints computer's choice.
	computer_choice = random.randint(0, 2)
	print('Computer chose: ')
	print(graphics[computer_choice])

	# Compares the choices to determine the winner or if it's a draw
	if player_choice == computer_choice:
	    print('It\'s a draw!') 
	elif player_choice == 0 and computer_choice == 2:
		print('You win!')
	elif player_choice == 2 and computer_choice == 0:
		print('You lose!')
	elif player_choice > computer_choice:
	    print("You win!")
	elif player_choice < computer_choice:
	    print("You lose!")

    # Player can play again or exit game and break out of the loop
	if not play_again():
		break