import os
import json

def readStory(story, chapterLevel, readerChoices):
    if chapterLevel == 1:
        chapterLevelString = "introduction"
        print(story[chapterLevelString]["description"])
        print("[1] " + story[chapterLevelString]["action1"])
        print("[2] " + story[chapterLevelString]["action2"])

    else:
        chapterLevelString = "chapter_"+str(chapterLevel)
        counter = 0
        while readerChoices != story[chapterLevelString][counter]["id"]:
            counter +=1

        print("[1] " + story[chapterLevelString][counter]["action1"])
        print("[2] " + story[chapterLevelString][counter]["action2"])

    while True:
        try:
            choice = int(input("Choice: "))-1
            readerChoices += str(choice)
            break
        except ValueError:
            print("please enter the value in [ ]")

    return readerChoices


def playGame(mainDirectory):
    print("You have chosen to play a game, the available games: \n")
    print(os.listdir(mainDirectory))

    while True:
        try:
            gameToPlay = input("The name of the file you want to play: ")
            gameFileName = mainDirectory + "/" + gameToPlay.capitalize() + "/" +gameToPlay.lower() + ".json"
            with open(gameFileName) as file:
                story = json.load(file)
            break
        except FileNotFoundError:
            print("File does not exist")

    print("COOL, now let's play the story !!\n")
    currentChapterLevel = 1
    totalLength = int(story["StoryLength"])
    readerChoices = "0b"

    for x in range(totalLength):
        readerChoices = readStory(story, currentChapterLevel, readerChoices)
        currentChapterLevel +=1

    print("The End, hoped you had fun !!")
