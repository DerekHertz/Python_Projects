#Number Guessing Game Objectives:
import random
from replit import clear

# Include an ASCII art logo.
logo = """ ___  __  __  ____  ___  ___  ____  _  _  ___     ___    __    __  __  ____ 
 / __)(  )(  )( ___)/ __)/ __)(_  _)( \( )/ __)   / __)  /__\  (  \/  )( ___)
( (_-. )(__)(  )__) \__ \\__ \ _)(_  )  (( (_-.  ( (_-. /(__)\  )    (  )__) 
 \___/(______)(____)(___/(___/(____)(_)\_)\___/   \___/(__)(__)(_/\/\_)(____)"""


def guessing_game():
  
  print(logo)
  
  # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
  choose_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
  
  #set values for lives (counter) alreadying including first guess
  if choose_level.lower() == 'easy':
    counter = 9
  else:
    counter = 4
  
  print(f"You chose {choose_level}, you have {counter + 1} lives")
  
  # Allow the player to submit a guess for a number between 1 and 100.
  user_guess = int(input("Choose a number between 1 and 100: "))
  
  #generate random number between 1 and 100
  comp_number = random.randint(1, 100)

  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
  while user_guess != comp_number:

    #check if out of lives before getting another input
    if counter < 1:
      print(f"You're out of lives :(. The number was {comp_number}.")
      play_again = input("Would you like to play again? Type 'y' or 'n': ")
      if play_again == 'y':
        clear()
        guessing_game()
      else:
        return 0

    #checks if user guess is too low or high and asks for another number
    else:
      if user_guess < comp_number:
        print("Too low.")
        user_guess = int(input("Choose a different number: "))
        # Track the number of turns remaining.
        counter -= 1
      elif user_guess > comp_number:
        print("Too high.")
        user_guess = int(input("Choose a different number: "))
        # Track the number of turns remaining.
        counter -= 1
  
  # If they got the answer correct, show the actual answer to the player with remaining lives.    
  print(f"You got it! The number was {comp_number}, you guessed it with {counter} lives left.")

  #check if players wants to play again
  play_again = input("Would you like to play again? Type 'y' or 'n': ")
  if play_again == 'y':
    clear()
    guessing_game()
  else:
    return 0

guessing_game()


