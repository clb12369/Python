print("Welcome to the Secret Auction.")

continue_bidding = True
auction = {}
highest_bid = {}


def find_highest_bidder(auction_dictionary):
    highest_bid = 0
    for bidder in auction_dictionary:
        bid_amount = auction_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")

while continue_bidding:

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    auction[name] = bid

    next_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if next_bid == 'no':
        continue_bidding = False
        find_highest_bidder(auction)
    elif next_bid == 'yes':
        print("\n" * 100)
