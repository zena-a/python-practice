# A password generator using random module and for loops

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the Pythonista Password Generator!')

# Prompt users for the number of letters, symbols, and numbers wanted for their password
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))
nr_symbols = int(input('How many symbols would you like to use?\n'))

# Order of characters are randomized for better security
password = []
user_password = ""

# Choose what letters, numbers, and symbols the password will consist of using random module
# Append the results to the password list
for c in range(nr_letters):
    password.append(random.choice(letters))

for n in range(nr_numbers):
    password.append(random.choice(numbers))

for s in range(nr_symbols):
    password.append(random.choice(symbols))

# Randomize the order of elements within the password list
random.shuffle(password)

# Adds items from list into one string in password2
for ch in password:
    user_password += ch 

# Print out user's password
print('\nYour generated password is:', user_password)