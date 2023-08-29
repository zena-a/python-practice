# Blackjack Game: Implementation of the classic blackjack game. Player competes against the computer dealer to reach a hand value as close to 21 as possible without exceeding it. 
# Built with custom functions for code readability and maintainability, and utilizes the 'random' module for card dealing. Organized with functions to handle card dealing, 
# score calculation, gameplay flow, and results comparison. 

import os, platform
import random
import ascii

# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Funcion to clear terminal screen
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Function to return a random card from the deck
def deal_card():
    return random.choice(cards)

# Function to calculate the total score in players' hand
def calculate_score(card_list):
    card_score = sum(card_list)
    if card_score == 21 and len(card_list) == 2:
        return 0 # represents blackjack

    if 11 in card_list and card_score > 21:
        card_list.remove(11)
        card_list.append(1)

    return card_score

# Function to compare scores and determine the winner
def compare_scores(user_score, comp_score):
    if user_score == comp_score:
        return "It's a draw!"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif comp_score == 0:
        return "Computer has Blackjack! You lose!"
    elif comp_score > 21:
        return "Computer went over. You win!"
    elif user_score > comp_score:
        return "You win!"
    else:
        return "You lose!"
    
# Function to ask if user wants to play again
def play_again():
    return input("Do you want to play again? Type 'y' or 'n': ").lower()    

# Main game function
def main():
    play = "y"

    while play == "y":
        clear()
        print(ascii.logo)

        # Initialize user and computer card lists
        user_cards = [deal_card(), deal_card()]
        computer_cards = [deal_card(), deal_card()]

        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)

        # Display the user's starting hand and one of the computer's cards
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Let the user draw cards until they want to pass or go over 21
        while user_score != 0 and input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            if user_score > 21:
                break
        
        # Let the computer draw cards until it reaches a score of at least 17 
        while comp_score != 0 and comp_score < 17:
            computer_cards.append(deal_card())
            comp_score = calculate_score(computer_cards)

        # Display final hands and scores
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Comuter's final hand: {computer_cards}, final score: {comp_score}")

        # Compare scores and determine the winner
        result = compare_scores(user_score, comp_score)
        print(result)

        # Ask if the play wants to play again
        play = play_again()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()