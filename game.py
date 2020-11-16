import random

def promptforNumber(minNum,maxNum):
  """Asks for the user to guess a number.

  Returns:
  -------
  int
  
  """
  return int(input(f"\nPick a number between {minNum} and {maxNum}: "))

def showWelcome(minNum,maxNum,tries):
  """Displays starting message.
  
  """
  print("Welcome to the guessing game.")
  print(f"The object of the game is to guess a number between {minNum} and {maxNum} within {tries} tries.")

def handleGuesses(answer,minNum,maxNum,tries):
  """Decides if the guess is valid.
  
  Parameters:
  -------
  answer

  """
  attempts = 0
  while attempts < tries:
    try:
      guess = promptforNumber(minNum,maxNum)
      if guess > answer:
        print("Smaller!")
      elif guess < answer:
        print("Larger!")
      else:
        print("Correct!")
        return
    except ValueError:
      print("You didn't enter an integer. Please try again.")
    except:
      print("I didn't understand that. Please try again.")
    finally:
      attempts+=1
  else:
    print(f"\nYou have run out of attempts. The answer was {answer}.")

def promptkeepPlaying():
  """Asks the player if they want to keep playing.
  
  Returns
  -------
  bool 
  
  """

  correctInput = False
  while not correctInput:
    ans = input("\nDo you want to keep playing (y/n): ")
    if ans == "y":
      return True
    elif ans == "n":
      return False


def run(minNum=1,maxNum=1000,tries=5):
  keepPlaying = True
  while keepPlaying:
    answer = random.randint(minNum,maxNum)
    showWelcome(minNum,maxNum,tries)
    handleGuesses(answer,minNum,maxNum,tries)
    keepPlaying = promptkeepPlaying()