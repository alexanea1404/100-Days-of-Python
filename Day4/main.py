
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice_human=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice_human >= 3 or choice_human <0 :
  print("You typed and invalid number")
else:
  list_option=[rock,paper,scissors]
  print(list_option[choice_human])

  choice_computer=random.randint(0,len(list_option)-1)
  print("Computer chose")
  print(list_option[choice_computer])

  if choice_human == choice_computer:
    print("Draw")
  elif (choice_human==0 and choice_computer==2) or (choice_human==1 and choice_computer==0) or (choice_human==2 and choice_computer==1):
    print("You won")
  else:
    print("You lose")
