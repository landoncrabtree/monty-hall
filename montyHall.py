#!/bin/bash

import random

class MontyHall():
    def __init__(self, carDoor):
        self.goatDoors = [1,2,3]
        self.goatDoors.remove(carDoor)
        self.carDoor = carDoor

# Setup
wins = 0
games = 0
switch = False
for i in range(1000):
    mh = MontyHall(random.randint(1,3)) # Create MontyHall object with specific car door.
    doorsLeft = [1,2,3] # Doors available: 1, 2, 3
    chosenDoor = random.randint(1,3) # Contestant picks door
    if (chosenDoor in mh.goatDoors): # If contestant chose goat door, reveal other goat door.
        tmp = mh.goatDoors
        tmp.remove(chosenDoor)
        doorsLeft.remove(tmp[0])
    else: # Otherwise, pick random goat door to reveal.
        doorsLeft.remove(random.choice(mh.goatDoors))
    if (switch):
        doorsLeft.remove(chosenDoor)
        chosenDoor = doorsLeft[0] # Select switch door.
    if (chosenDoor is mh.carDoor):
        wins += 1
    games += 1

winRate = round((wins/games)*100)
print("Wins:" + str(wins))
print("Games:" + str(games))
print("Win Rate: " + str(winRate) + "%")
