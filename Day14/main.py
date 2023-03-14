#Import the data, logo and random
import art
from game_data import data
import random
from replit import clear

#Print logo
print(art.logo)


#Get data from random account
def get_random_account():
    return random.choice(data)

#Compare the number of followers for the two accounts
def check_answer(celebrity1, celebrity2):
    if celebrity1["follower_count"] > celebrity2["follower_count"]:
        return celebrity1["name"]
    elif celebrity2["follower_count"] > celebrity1["follower_count"]:
        return celebrity2["name"]
    else:
        return 0

#Format data into printable format: name, description, country
def format_data(celebrity1, celebrity2):
    print(
        f"Compare A: {celebrity1['name']}, a {celebrity1['description']} from {celebrity1['country']} "
    )
    print(art.vs)
    print(
        f"Against: {celebrity2['name']}, a {celebrity2['description']} from {celebrity2['country']} "
    )

def game():
  celebrity_1 = get_random_account()
  celebrity_2 = get_random_account()
  score = 0

  continue_game = True

  while continue_game:
      celebrity_1 = celebrity_2
      celebrity_2 = get_random_account()

      if celebrity_1 == celebrity_2:
         celebrity_2 = get_random_account(data)

      print(celebrity_1["follower_count"], celebrity_2["follower_count"])
      format_data(celebrity_1, celebrity_2)
      answer = input("Who has more followers? Type 'A' or 'B': ").lower()

      if answer == "a":
          user_pick = celebrity_1["name"]
      elif answer == "b":
          user_pick = celebrity_2["name"]
      else:
         print("Sorry. You lost.")

      compare_result = check_answer(celebrity_1, celebrity_2)
      clear()
      print(art.logo)
      if user_pick == compare_result:
          score += 1
          print(f"You're right! Current score:{score}.")
      else:
          print(f"Sorry you lost. Your final score is {score}")
          continue_game = False
    
game()