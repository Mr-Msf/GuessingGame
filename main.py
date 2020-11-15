
def promptforNumber():
  """Asks for the user to guess a number.

  Returns:
  -------
  int
  
  """
  return int(input("\nPick a number between 1 and 1000: "))

def showWelcome():
  """Displays starting message.
  
  """
  print("Welcome to the guessing game.")
  print("The object of the game is to guess a number between 1 and 1000 within 5 tries.")

def handleGuesses(answer):
  """Decides if the guess is valid.
  
  Parameters:
  -------
  answer

  """
  attempts = 0
  while attempts < 5:
    try:
      guess = promptforNumber()
      if guess > answer:
        print("Smaller!")
      elif guess < answer:
        print("Larger!")
      else:
        print("Correct!")
    except ValueError:
      print("You didn't enter an integer. Please try again.")
    except:
      print("I didn't understand that. Please try again.")
    finally:
      attempts+=1

def main():
  answer = 678
  showWelcome()
  handleGuesses(answer)

if __name__ == "__main__":
  main()