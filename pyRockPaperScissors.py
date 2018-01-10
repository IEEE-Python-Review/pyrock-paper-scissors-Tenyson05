import random

def play():
  if(selection == 1):
    return "Rock"
  elif(selection == 2):
    return "Paper"
  elif(selection == 3):
    return "Scissors"

def Computer():
  comChoice = random.randint(0, 2)
  if(comChoice == 0):
    comPlay = "Rock"
    return comPlay
  elif(comChoice == 1):
    comPlay = "Paper"
    return comPlay
  elif(comChoice == 2):
    comPlay = "Scissors"
    return comPlay     
  """This function should simply return the computers SINGLE choice of rock, paper, or scissors IN LOWERCASE"""

def Human():
  global selection
  print("1. Rock")
  print("2. Paper")
  print("3. Scissors")
  selection = int(input("Choose the number that corresponds with the move you want to make" + " "))
  if selection == 1:
    print("Rock".lower())
  elif selection == 2:
    print ("Paper".lower())
  elif selection == 3:
    print("Scissors".lower())
  else:
    print ("Invalid play")

def main():
	print("Welcome To PyRock Paper Scissors Best of 3\n")
	"""
  This function should prompt the player to enter his/her name, get the player's and computer's play, displays what the player and the 
  computer played and displays who won. Remember this is a best of 3 match so this function should also keep track of who won each round 
  and displays the final scores and the overall winner.
  """
	
if __name__ == '__main__':
        main()
        name = input("Enter Name" + " ")
        nameScore = 0
        ComputerScore = 0

        for x in range(0, 3):
          Human()
          
          print(play()+ " " + "vs" + " " +Computer())

          if(play() == Computer()):
            print("Draw!")
          elif(play() == "Rock"):
            if(Computer() == "paper"):
              print("The computer won")
            ComputerScore =  ComputerScore + 1
          elif(play() == "Rock"):
            if(Computer == "Scissors"):
              print(name, "won")
              nameScore = nameScore + 1        
          elif(play() == "Scissors"):
            if(Computer() == "Paper"):
              print(name, "won")
              nameScore = nameScore + 1
          elif(play() == "Scissors"):
             if(Computer() == "Rock"):
               print("The computer won")
               ComputerScore = ComputerScore + 1
          elif(play() == "Paper"):
              if(Computer() == "Rock"):
                print(name, "won")
                nameScore = nameScore + 1
          elif(play() == "Paper"):
            if(Computer() == "Scissors"):
              print("The computer won")
              ComputerScore = ComputerScore + 1

          print(nameScore)
          print(ComputerScore)
          if(nameScore > ComputerScore):
            print(name, "has won with", nameScore)
          else:
            print("The computer has won with", ComputerScore)


           

            

              
                     












               
        
