import random
import person
import Emailer
import time

participants = []

numPlayers = int(input("Enter the number of players playing: "))
namesInputted = 0

while namesInputted != numPlayers:

    inputName = input("Enter the player name: ")
    emailAddress = input("Enter " + inputName + "'s email address: ")

    newPerson = person.person(inputName, emailAddress)
    participants.append(newPerson)
    namesInputted += 1



random.shuffle(participants)
assignments = []



def assignFunction():
    for i in range(numPlayers):
        giver = participants[i]
        assignmentIndex = (i + 1) % numPlayers
        reciever = participants[assignmentIndex]
        assignments.append((giver, reciever))
        Emailer.sendEmail(giver.name, giver.email, reciever.name)
        time.sleep(1)


assignFunction()




