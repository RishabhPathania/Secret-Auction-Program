import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

import art
print(art.logo)
print("Welcome to the secret aution program.")
collegues=True
bidder={}
while collegues:
  name=input("What is your name?: ")
  bid=int(input("What's your bid? $"))
  more_players=input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if more_players=="no":
    collegues=False
  clear()
  bidder[name]=bid
max_bid=0
for key in bidder:
  if bidder[key]>max_bid:
    max_bid=bidder[key]
    winner=key
print(f"The Winner of the Auction is {winner} with a bid of ${max_bid}.")
    
  
  
  