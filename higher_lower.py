import random
from replit import clear
from art import logo, vs
from game_data import data

#format account data into printable format
def format_account(account):
  """Takes the account data and returns printable format"""
  name = account['name']
  description = account['description']
  country = account['country']

  return f"{name}, a {description}, from {country}."


def check_answer(guess, a_follower_count, b_follower_count):
  """Use if statement to check user is correct"""
  if a_follower_count > b_follower_count:
    return guess == 'a'
  else:
    return guess == 'b'


#display art
print(logo)
score = 0
game_cont = True
account_b = random.choice(data)
#generate a random account from the game data

while game_cont == True:
  account_a = account_b
  account_b = random.choice(data)
  
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_account(account_a)}")
  print(vs)
  print(f"Against B: {format_account(account_b)}")
  
  #ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B'.").lower()
  
  #check if user is correct
  ##get follower count of each account
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  ##use if statement to check if user is correct
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
  
  #give user feedback on their guess

  #clear screen
  clear()
  print(logo)
  
  #score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry you're wrong. Final score: {score}")
    game_cont = False
    