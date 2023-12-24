############### Blackjack Project #####################
import random

def print_intro():
  msg="""
  .------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
  print(msg)
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
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

print_intro()

def get_card():
  return cards[random.randint(0,len(cards)-1)]
  
yourCards =[]
computerCards=[]

def play_again():
  x = input("Do you want to play a game of Blackjack? Type 'y' or'n':")
  if x =='y' : return True
  return False

def another_card():
  x = input("Type 'y' to get another card, type 'n' to pass:")
  if x =='y' : return True
  return False

def print_status():
  print(f"Your cards: {yourCards}, current score: {sum(yourCards)}")
  if len(computerCards) >0:
    print(f"Computer's first card: {computerCards[0]}.  She has {len(computerCards)} cards")  

def print_final_status():
  print(f"Your final hand: {yourCards}, final score: {sum(yourCards)}")
  print(f"Computer's final hand: {computerCards}, final score {sum(computerCards)}")  

  if over_21(yourCards):
    print("You went over. You Loose \U0001F641 ")
  elif sum(yourCards) == sum(computerCards):
    print("Draw...")
  elif over_21(computerCards):
    print("Dealer went over... You Win!!")
  elif sum(computerCards) < sum(yourCards):
    print("your win!")
  else:
    print("Dealer wins.")
    

def get_cards(list,numCards):
  for i in range(0,numCards):
    list.append(get_card())

def over_21(list):
  return sum(list)>21

def new_game():
  yourCards.clear()
  computerCards.clear()
  get_cards(yourCards,2)
  get_cards(computerCards,2)
  print_status()

while play_again() == True:
  new_game()
 
  while not over_21(yourCards) and another_card():
    get_cards(yourCards,1)
    print_status()

  while not over_21(computerCards) and sum(computerCards)<=16 :
    get_cards(computerCards,1)

  print_final_status()

