import os
import CreateGame
import PlayGame


print("Welcome to the game where you are the hero !!\nFirst thing first,\n")
mainDirectory = "null"
while not(os.path.exists(mainDirectory)):
    mainDirectory = input("please put in the directory where the stories will be loaded in: ")

while True:
    condition = False
    while not condition:
        actionChoice = input(
            "do you want to: \n[1] make a new story\n[2] play a story (only possible if you have a story)\n[3] Exit game\n")
        if actionChoice == "1" or (actionChoice == "2" and os.listdir(mainDirectory)):
            condition = True
        elif actionChoice == "3":
            condition = True

    if actionChoice == "1":
        CreateGame.createGame(mainDirectory)
    elif actionChoice == "2":
        PlayGame.playGame(mainDirectory)
    elif actionChoice == "3":
        print("Game Exited")
        break
