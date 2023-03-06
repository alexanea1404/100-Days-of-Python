from replit import clear
from art import logo
print(logo)

def choose_winner(bidding_dict):
  max_bid = 0
  winner_name = ""
  for bid_value in bidding_dict:
      if bidding_dict[bid_value] > max_bid:
        max_bid = bidding_dict[bid_value]
        winner_name = bid_value
  print(f"The winner is {winner_name} with a bid of ${max_bid}")

check_bid = True
auction_dict = {}

while check_bid == True :
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  auction_dict[name] = bid
  other_biders = input("Are there any other bidders. Type 'yes' or 'no'.").lower()
  if other_biders == "no":
    check_bid = False
    choose_winner(auction_dict)
  elif other_biders == "yes":
    clear()


