import random
def thegame():
  print("Hello and welcome to my word guessing game")
  print("You need to guess a number between 1 and 100.")
  int(input("Select the amount of lives you want") = lives
  thenumber = random.randint(1,100)
  while lives > 0:
    int(input("Guess the number. Lives remaining: " + lives) = guess
    if guess == thenumber:
      print("Congrats :celebrateemoji:")
      lives = 0
      guessedcorrect = True
    else:
      print("Not correct.")
      lives -= 1
  if guessedcorrect == False:
    print("Oops you ran out of lives")
  input("Try again? True/False") = Restart
  if Restart == 1:
    thegame()
    
