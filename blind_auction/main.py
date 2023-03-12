import os
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
print("Welcome to the secret auction program.")

end_of_bids = False

def find_the_winner(all_records):
  highest_result = 0
  winner =""
  for bidder in all_records:
    result = all_bidders[bidder]
    if result > highest_result:
      highest_result = result
      winner = bidder
  print(f"The winner is {winner} with the bid of ${highest_result}.")
    

while not end_of_bids:
  all_bidders = {}
  name = input("What's your name? ")
  bid = int(input("What's your bid? $"))
  all_bidders[name] = bid

  
  another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

  if another_bidder == "no":
    end_of_bids = True
  if another_bidder == "yes":
    os.system('clear')

  find_the_winner(all_bidders)



