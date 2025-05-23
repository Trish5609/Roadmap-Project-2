import random
def thegame():
  print("Hello and welcome to my word guessing game")
  print("You need to guess a number between 1 and 100.")
  lives = int(input("Select the amount of lives you want |"))
  thenumber = random.randint(1,100)
  guessedcorrect = False
  res = False
  while lives > 0:
    guess = int(input("Guess the number. Lives remaining: " + str(lives) + "|"))
    if guess == thenumber:
      print("Congrats :celebrateemoji:")
      lives = 0
      guessedcorrect = True
    else:
      if guess > thenumber:
        print("Too big")
      if guess < thenumber:
        print("Too small")  
      lives -= 1
  if guessedcorrect == False:
    print("Oops you ran out of lives")
  res = bool(input("Try again? (Leave blank if no)"))
  if res == True:
    thegame()
  elif res == False:
    print("Thank-a you so much-a for playing ma game!")
thegame()
