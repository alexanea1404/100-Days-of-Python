############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
from replit import clear
import random

print(logo)

def deal_card(card_list):
  """Returns a random card from the deck."""
  return random.choice(card_list)

def calculate_score(cards_list):
  """Take a list of cards and return the score calculated from the cards"""
  score = sum(cards_list)
  if score == 21 and len(cards) == 2:
    return 0
  if 11 in cards_list and score > 21:
    cards_list.remove(11)
    cards_list.append(1)
  return score

def compare(score_user, score_computer):
  if score_user == score_computer:
    print("Draw")
  elif score_computer == 0:
    print("You lost")
  elif score_user == 0:
    print("You won")
  elif score_user > 21:
    print("You lost")
  elif score_computer > 21:
    print("You win")
  elif score_user > score_computer:
    print("You win")
  else:
    print("You lost")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
  user_cards = []
  computer_cards = []
  #_ when we don't care about the iteration name
  for _ in range(2):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))

  flag_play = True
  while flag_play:
    score_user = calculate_score(user_cards)
    score_computer = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {score_user}")
    print(f"Computer's first card: {computer_cards[0]}")
    if score_user == 0 or score_computer == 0 or score_user > 21:
      flag_play = False
    else:
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if(another_card == "y"):
        user_cards.append(deal_card(cards))
      else: 
        flag_play = False

  while score_computer != 0 and score_computer < 17:
    computer_cards.append(deal_card(cards))
    score_computer = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {score_user}")  
  print(f"Computer's final hand: {computer_cards}, final score: {score_computer}")
  compare(score_user,score_computer)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
