# Author: Kevin Johnson
# Created date: DEC 02 2023

# Advent of Code 2023
# DAY 02 PART 01

# Answer 2285

from sys import argv
import re

script, input_file = argv

possibleGameCount = 0

maxCubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def createDict(cubeSet):
    cubeDict = {}
    for cubeSetItem in cubeSet:
        singleCube = list(map(str.strip, cubeSetItem.split()))
        cubeDict[singleCube[1]] = int(singleCube[0])
    return cubeDict

def checkGameRounds(gameRounds):
    global maxCubes
    isPossible = True
    for gameCubes in gameRounds:
        singleRound = list(map(str.strip, gameCubes.split(',')))
        #print(singleRound)
        cubeDict = createDict(singleRound)
        for key in cubeDict:
            if cubeDict[key] > maxCubes[key]:
                isPossible = False
                break
    return isPossible

with open(input_file) as openfileobject:
    for line in openfileobject:
        cleanline = line.strip()
        gameData = cleanline.split(':')
        gameRounds = list(map(str.strip, gameData[1].split(';')))
        #print(gameRounds)
        print(gameData[0], str(checkGameRounds(gameRounds)))
        if checkGameRounds(gameRounds):
            possibleGameCount = possibleGameCount + int(gameData[0].split()[1])

print(possibleGameCount)