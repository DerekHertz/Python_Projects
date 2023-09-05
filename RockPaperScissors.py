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

#Write your code below this line 👇
game_choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
comp_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
  print("Invalid number. You lose.")
else:
  print("You chose: \n")
  print(game_choices[user_choice])
  print("Computer chose: \n")
  print(game_choices[comp_choice])
  if user_choice == 0 and comp_choice == 1 and comp_choice != 0:
    print("You lose.")
  elif user_choice == 1 and comp_choice == 2 and comp_choice != 1:
    print("You lose.")
  elif user_choice == 2 and comp_choice == 0 and comp_choice != 2:
    print("You lose.")
  elif user_choice == comp_choice:
    print("Tie.")
  else:
    print("You win.")
