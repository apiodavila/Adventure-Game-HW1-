### initial code structure and story taken from www.makeuseof.com ###
#Alberto Pio Davila "Retro Text Adventure" Final Project#

count_killed = 0
weapon = False # we will have a weapon variable that you may or may not find which affects the outcome of some situatuations#
import pandas as pd
def introScene():
    
  global count_killed   
  directions = ["left","right","forward"]
  print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    if userInput == "left":
      showShadowFigure()
    elif userInput == "right":
      showSkeletons()
    elif userInput == "forward":
      hauntedRoom()
    elif userInput == "backward":
      print("You find that this door opens into a wall.")
    else: 
      print("Please enter a valid option.")

def showShadowFigure():
  directions = ["right","backward"]
  print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      cameraScene()
    elif userInput == "left":
      print("You find that this door opens into a wall.")
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")
      
def cameraScene():
  directions = ["forward","backward"]
  print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      print("You made it! You've found an exit.")
      
      print('you died',count_killed, 'times')
      try:
          with open('game.txt','a') as f:#this will log your game history so you can compare your runs#
              f.write(str(count_killed)+'\n')
      except:
          print('your file is in the wrong directory')
      deathsDF = pd.read_csv('game.txt')
      deathsDF.columns = ['# of deaths']#the data frame is divided into number of deaths and which attempt you are on#
      print(deathsDF)
      quit()
    elif userInput == "backward":
      showShadowFigure()
    else:
      print("Please enter a valid option.")
      
def hauntedRoom():
  global count_killed
  directions = ["right","left","backward"]
  print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      print("Multiple goul-like creatures start emerging as you enter the room. You are killed. ------ Try Again")
      count_killed += 1
      introScene()
    elif userInput == "left":
      print("You made it! You've found an exit.")
      print('you died',count_killed, 'times')
      try:
          with open('game.txt','a') as f:
              f.write(str(count_killed)+'\n')
      except:
          print('your file is in the wrong directory')
      deathsDF = pd.read_csv('game.txt')
      deathsDF.columns = ['# of deaths']
      print(deathsDF)
      quit()
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")

def showSkeletons():
  global count_killed
  directions = ["backward","forward"]
  global weapon
  print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/backward/forward")
    userInput = input()
    if userInput == "left":
      print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
      weapon = True
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print("Please enter a valid option.")
def strangeCreature():
  global count_killed
  actions = ["fight","flee"]
  global weapon
  print("A strange goul-like creature has appeared. You can either run or fight it. What would you like to do?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
        print('you died',count_killed, 'times')
        try:
          with open('game.txt','a') as f:
              f.write(str(count_killed)+'\n')
        except:
          print('your file is in the wrong directory')
        deathsDF = pd.read_csv('game.txt')
        deathsDF.columns = ['# of deaths']
        print(deathsDF)
        quit()
      else:
        print("The goul-like creature has killed you.------ Try again")
        count_killed += 1
      introScene()
    elif userInput == "flee":
      showSkeletons()
    else:
      print("Please enter a valid option.")

if __name__ == "__main__":
  while True:
    print("Welcome to my Adventure Game!")
    print("As an avid traveler, you have decided to visit the Catacombs of Paris.") 
    print("However, during your exploration, you find yourself lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    introScene()

#Khan, Sharlene. “How to Create a Text Based Adventure Game in Python.” MUO, 13 Aug. 2022, https://www.makeuseof.com/python-text-adventure-game-create/. 