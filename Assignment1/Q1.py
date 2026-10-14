import random
def play_bounded_guessing_game():
  secret_number = random.randint(1,10)
  for i in range(1,3):
   guess =  input("Guess the number 1-10")
   if(guess == secret_number):
     print("Congratulations! You won")
     return
   else:
     print("Wrong guess! Try again.")
  print("Game Over! The secret number was",secret_number,".")
  