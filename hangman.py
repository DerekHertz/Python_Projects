import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#create 'empty' list length of random word
insert_letter = ['_'] * len(chosen_word)

#count _ in insert_letter after determining length to decrement in while loop
underscore = insert_letter.count("_")

#set num of lives, decrements in while loop
lives = 7

#goes through loop until wins or loses
while underscore > 0 and lives > 0:
    guess = input("Guess a letter: ").lower()    
    #determine if guess does not exist in chosen_word
    wrong = False
    for letter in chosen_word:
        #check if guess does exist in chosen_word
        if guess == letter:
            wrong = True
    if wrong == False:
        #removes life if not in chosen_word, prints hangman stage
        lives -= 1
        print(stages[lives])
        #if ran out of lives you lose
        if lives == 0:
            print("You lost, womp womp")
    #if letter is in chose_word, places in correct corresponding index into insert_letter and displays output
    for letter_index in range(0, (len(chosen_word))):
        if chosen_word[letter_index] == guess:
            insert_letter[letter_index] = chosen_word[letter_index]
            #decrementing underscore to determine if user has guessed entire word
            underscore -=1
    print(insert_letter)
    #if user guessed entire word (no underscores remaining) user wins
    if underscore == 0:
        print(f"You won! The word was {chosen_word}.")

