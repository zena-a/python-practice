# Highest Bidder: A bling auction using a dictionary that stores the bidder's name and their bid.
# It compares all the bids to find the highest one.

from clearscreen import clear

# Function to find and display the highest bidder
def find_highest_bidder(bidders):
    highest_bid = 0 
    winner = ''

    for name in bidders:
        if bidders[name] > highest_bid:
            highest_bid = bidders[name]
            winner = name
    print(f'The winner is {winner} with a bid of ${highest_bid}')

bidders = {}

# Main bidding loop
while True:
    name = input('What\'s your name?: ')
    bid = int(input('What is your bid?: $'))
    bidders[name] = bid

    bid_again = input('Are there any other bidders? Type \'yes\' or \'no\': ').lower()
    if bid_again == 'no':
        break
    else:
        clear()

# Call the function for highest bidder
find_highest_bidder(bidders)