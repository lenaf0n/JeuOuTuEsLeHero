import json
import os

def writeToJSONFile(filePathName,  data):
    try :
        with open(filePathName) as fp:
            listObj = json.load(fp)
            listObj.update(data)
    except FileNotFoundError:
        listObj = data

    with open(filePathName, 'w') as write_file:
        json.dump(listObj, write_file)

def writeChoiceToChapter (filePathName, chapterLevelString, data) :
    with open(filePathName, 'r+') as file:
        file_data = json.load(file)
        file_data[chapterLevelString].append(data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def readChoiceAboveWrite(filePathName, currentChapterLevel, choice, counter):
    with open(filePathName) as file:
        data = json.load(file)

    chapterLevelString = "chapter_"+str(currentChapterLevel-1)

    if choice == 0:
        actionChoice = "action1"
    else:
        actionChoice = "action2"

    if currentChapterLevel == 2:
        print("Here is the scenarios that will lead to the two choices :")
        print(data["introduction"][actionChoice] + "\n")
    else:
        print("Here is the scenarios that will lead to the two choices :")
        print(data[chapterLevelString][counter][actionChoice] + "\n")


def createNewGame(nameOfStory, directory):
    print("So how will this work, everytime you will be asked a story, where you will enter the first scenario.")
    print("And then the two possible choices it could lead to, you will need to enter each time two new choices.")
    print("when you have reached the final choice, end the story and enter the ending for each choices")
    print("good luck with creating your game, and most importantly have fun!")

    path = os.path.join(directory, nameOfStory.capitalize())
    os.mkdir(path)

    path = path + '/' + nameOfStory + '.json'

    print("Now that everything is set up, let's start the story...")
    return path

def createChapter(chapterLevel, filePathName):
    totalPagesForChapter = pow(2, chapterLevel)
    chapterLevelString = "chapter_"+str(chapterLevel)

    data = {
        chapterLevelString: []
    }

    data = eval(str(data))

    writeToJSONFile(filePathName, data)

    counter = 0
    num = 0
    for x in range(int(totalPagesForChapter/2)):
        createPage(chapterLevel, chapterLevelString, x, filePathName, counter, num)
        if (x%2==1):
            counter +=1
            num = 0
        else:
            num=1


def createPage(chapterLevel, chapterLevelString, n, filePathName, counter, num):
    readChoiceAboveWrite(filePathName, int(chapterLevelString[-1]), num, counter)
    choice1 = input("enter the first choice: ")
    print("\n")
    choice2 = input("enter the second choice: ")

    data = {
        "id": str(format(n, '#0' + str(chapterLevel + 1) + 'b')),
        "action1": choice1,
        "action2": choice2
    }

    writeChoiceToChapter(filePathName, chapterLevelString, data)

def createGame(mainDirectory):
    fileName = input("Before getting started, what is the story called: ")
    gamePath = createNewGame(fileName, mainDirectory)

    introToStory = input("The story needs to begin somewhere, intro: ")
    choice1 = input("enter the first choice of the story: ")
    choice2 = input("enter the second choice of the story: ")

    story = {
        "introduction": {
            "description": introToStory,
            "action1": choice1,
            "action2": choice2
        }
    }
    writeToJSONFile(gamePath, story)

    actionTaken = input("Do you want to: \n[1] New Chapter\n[2] End the story\n")

    chapterLevel = 1

    while actionTaken != "2":
        chapterLevel += 1
        if actionTaken == "1":
            createChapter(chapterLevel, gamePath)
        actionTaken = input("Do you want to: \n[1] New Chapter\n[2] End the story\n")

    data = {
        "StoryLength": chapterLevel
    }
    writeToJSONFile(gamePath, data)

    print("You finished creating the story!!")
