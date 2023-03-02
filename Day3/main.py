print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1=input("You are at a cross road. Where do you want to go: left <--- or right? ---> \n").lower()

if choice1 == "left":
  choice2 = (input("Go ahead until you get to the water. You are in front of lake and the island is in the middle of the lake. Type 'swim' to swim across the lake or 'boat' to wait for the boat.\n ")).lower()
  if choice2 == "boat":
    print("You are on the island. You found a key in the sand. Let\'s continue our adventure!")
    choice3 = input("You walk until you get to a castle. There are 3 doors: one red, one yellow and one green. The key works only in one of them. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of snakes. Game over!")
    elif choice3 == "yellow":
      print ("You enter a room of beasts. Game Over.")
    elif choice3 == "green":
      print("You found the treasure")
    else:
      print("You chose a door that doesn't exist. Game Over!")
  else:
    print("You were eaten by crocodiles. Game Over!")
else:
  print("You were attacked bu wolves. Game Over!")
