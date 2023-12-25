#Number Guessing Game Objectives:

# Include an ASCII art logo.
import art
import random

def get_input(prompt, default_value):
  user_input = input(prompt)
  if user_input == '':
      return default_value
  else:
      return user_input
    #https://patorjk.com/software/taag/#p=display&f=Star%20Wars&t=Guessing...
print(art.title)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")
level = get_input("Choose a difficulty. Type 'easy' or 'hard': (easy)",'easy')
if level == 'easy':
  attempts = 10
else:
  attempts = 5
  
while attempts >0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess:"))
  if guess == number:
    print(f"You got it! The answer was {number}.")
    attempts =0
  elif guess > number:
    print("Too high.")
  elif guess < number:
    print("To low.")

  attempts -= 1
  if attempts >0:
    print("Guess again.")

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

