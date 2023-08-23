# Caesar Cipher: Implements the classic Caesar Cipher technique, an encryption method. 
# Takes user input for a message, and a shift value, that will allow for both encryption and decryption. 
# Demonstrates funademental cryptography concepts and the manipulation of strings in Python. 

# Function to perform Caesar Cipher encryption and decryption
def caesar_cipher(text, shift, direction):
    result = ''
    shift %= 26 # Handle shifts greater than the alphabet length

    if direction == 'decode':
        shift = -shift # Adjust shift for decoding

    for char in text:
        if char.isalpha():
            if char.isupper():
                # ord(char) returns the ASCII value of a character
                # chr(ascii_value) converts an ASCII value back to it's corresponding character
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) # Shift uppercase letters
            else:
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97) # Shift lowercase letters
            result += shifted_char
        else:
            result += char

    print(f'Here\'s the {direction}d result: {result}\n')

print('CAESAR CIPHER ENCRYPTION AND DECRYPTION')

# Continues to prompt user for input and keep srunning until the user decides to exit
while True:
    direction = input('Type \'encode\' to encrypt, \'decode\' to decrypt:\n').lower()
    text = input('Type your message:\n').lower()
    shift_num = int(input('Type the shift number:\n'))

    # Validate the input direction
    if direction == 'encode' or direction == 'decode':
        caesar_cipher(text, shift_num, direction)
    else:
        print('You have entered an invalid value.')

    result = input('Type \'yes\' if you want to go again. Otherwise type \'no\'\n').lower()

    if result == 'no':
        print('Goodbye!')
        break