import random

name = []

numPlayers = int(input("Enter the number of players playing: "))
namesInputted = 0

while namesInputted != numPlayers:

    inputName = input("Enter the player name: ")
    name.append(inputName)
    namesInputted += 1



random.shuffle(name)
assignments = []



def assignFunction():
    for i in range(numPlayers):
        giver = name[i]
        assignmentIndex = (i + 1) % numPlayers
        reciever = name[assignmentIndex]
        assignments.append((giver, reciever))


assignFunction()


