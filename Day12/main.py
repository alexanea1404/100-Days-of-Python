#Number Guessing Game
from art import logo
import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_level_difficulty(level_type):
  if level_type == "easy":
    return EASY_LEVEL_ATTEMPTS
  elif level_type == "hard":
    return HARD_LEVEL_ATTEMPTS
  else:
    print("Please try again")

def comparison(user_number, guess_number, attempts):
  """Compare the random number to the guess"""
  if user_number > guess_number:
    print("Too high")
    return attempts -1
  elif user_number < guess_number:
    print("Too low")
    return attempts -1
  else:
    print(f"You got it! The answer was {guess_number}.")
    
def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  random_number = random.randint(1,100)
  level = input("Choose dificulty level 'easy' or 'hard': ").lower()

  #Number of attempts based on the level  
  attempts = set_level_difficulty(level)
  guess = 0
  while guess != random_number:
    print(f"You have {attempts} remaining to guess the number")
    guess = int(input("Make a guess:"))
    
    attempts = comparison(guess, random_number, attempts)
    if attempts == 0:
      print("You lost")
      return
    elif guess != random_number:
     print("Guess again")
      
game()

