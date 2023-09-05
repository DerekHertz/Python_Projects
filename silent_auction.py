from replit import clear
#HINT: You can call clear() to clear the output in the console.
print("Welcome to the secret auction program.")
#create empty list
bidders = {}

#function to add keys and values as nested dictionary to empty list
def add_bidders():
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders[name] = bid

other_bidders = 'yes'

#while loop for adding more bidders
while other_bidders.lower() == 'yes':
  clear()
  add_bidders()
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

#find persone(key) with max value and fprint key with value in final statement
for key in bidders:
  if bidders[key] == max(bidders.values()):
    print(f"The winner is {key} with a bid of ${bidders[key]}")
  
  


