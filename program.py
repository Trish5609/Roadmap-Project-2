import random
# Instead of the difficulty level this code allows the user to select the number of lives they get. I also added a highscore feature and a replay feature.
highScore = 999
def thegame():
  print("Hello and welcome to my word guessing game")
  print("You need to guess a number between 1 and 100.")
  lives = int(input("Select the amount of lives you want |"))
  inL=lives
  thenumber = random.randint(1,100)
  guessedcorrect = False
  res = False
  while lives > 0:
    guess = int(input("Guess the number. Lives remaining: " + str(lives) + "|"))
    if guess == thenumber:
      print("Congrats :celebrateemoji:")
      guessedcorrect = True
      global highScore
      if inL-lives+1<highScore:
        highScore = inL-lives+1
        print("You beat your PB!")
      print("Your personal best: " + str(highScore) + " guesses.")  
      lives = 0
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
