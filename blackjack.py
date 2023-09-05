############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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
import random

def blackjack():
  
  start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  while start_game == 'y':
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    user_cards = [random.choice(cards), random.choice(cards)]
    
    temp_score = sum(user_cards)
    
    comp_cards = [random.choice(cards), random.choice(cards)]
    
    comp_score = sum(comp_cards)
    
    if temp_score == 21 and comp_score < 21:
      print(f"Your cards: {user_cards}, current score: {temp_score}\nComputer's cards: {comp_cards}, current score: {comp_score}\nBlackjack! You win.")
      return 0
  
    while comp_score < 17:
      comp_cards.append(random.choice(cards))
      comp_score = sum(comp_cards)

    print(f"Your cards: {user_cards}, current score: {temp_score}\nComputer's first card: {comp_cards[0]}")
    
    draw_another = input("Type 'y' to get another card, type 'n' to pass: ")

    while draw_another == 'y' and temp_score < 21:
      user_cards.append(random.choice(cards))
      temp_score = sum(user_cards)
      print(f"Your cards: {user_cards}, current score: {temp_score}\nComputer's first card: {comp_cards[0]}.")
      if temp_score < 21:
        draw_another = input("Type 'y' to get another card, type 'n' to pass: ")
        
    if (temp_score <= 21 and comp_score < 21 and temp_score > comp_score) or (temp_score <= 21 and comp_score > 21):
      print(f"Your final hand: {user_cards}, final score: {temp_score}.\nComputer's final hand: {comp_cards}, final score: {comp_score}")
      print("You win!")
    elif temp_score == comp_score and temp_score < 21 and comp_score < 21:
      print(f"Your final hand: {user_cards}, final score: {temp_score}.\nComputer's final hand: {comp_cards}, final score: {comp_score}")
      print("Draw!")
    else:
      print(f"Your final hand: {user_cards}, final score: {temp_score}.\nComputer's final hand: {comp_cards}, final score: {comp_score}")
      print("You lose!")
      
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
blackjack()
