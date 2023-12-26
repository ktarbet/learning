import random
import art
from game_data import data

game_info ={ 'A' : "",'B': "", 'score':0 }

def get_rand():
  return random.randint(0,len(data)-1)

def intro(game_info):
  print(art.logo)
  game_info['A'] = data[get_rand()]
  game_info['B'] = data[get_rand()]
  game_info['score'] = 0

  
def show_two_entries(game_info):
  print(f"Compare A: {game_info['A']['name']}, a {game_info['A']['description']},from {game_info['A']['country']}")
  print(art.vs)
  print(f"Against B: {game_info['B']['name']}, a {game_info['B']['description']},from {game_info['B']['country']}")
  
def check(choice, info):
  A=info['A']
  B=info['B']
  correct=True
  score = info['score']
  if choice == 'A' and  A['follower_count'] >= B['follower_count']:
    score += 1
  elif choice == 'B' and  B['follower_count'] > A['follower_count']:
    score += 1
  else:
    correct = False

  game_info['score'] = score
  if correct:
    print(f"You're right! Current score: {score}")
    info['A'] = B
    info['B'] = data[get_rand()]
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
  return correct

play_again= True
while play_again:
  intro(game_info)
  correct = True
  
  while correct:
    show_two_entries(game_info)
    choice = input("Who has more followers? Type 'A' or 'B':")
    correct = check(choice,game_info)

  play_again = input("play again y/n:") =='y'
