# Author: Kevin Johnson
# Created date: DEC 02 2023

# Advent of Code 2023
# DAY 02 PART 02

# Answer 77021

from sys import argv
import re

script, input_file = argv

powerSum = 0

def createDict(cubeSet):
    cubeDict = {}
    for cubeSetItem in cubeSet:
        singleCube = list(map(str.strip, cubeSetItem.split()))
        cubeDict[singleCube[1]] = int(singleCube[0])
    return cubeDict

def checkGameRounds(gameRounds):
    powerDict = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    powerValue = 1
    for gameCubes in gameRounds:
        singleRound = list(map(str.strip, gameCubes.split(',')))
        # print(singleRound)
        cubeDict = createDict(singleRound)
        for key in cubeDict:
            if cubeDict[key] > powerDict[key]:
                powerDict[key] = cubeDict[key]
    for val in powerDict.values():
        powerValue = powerValue * val
    return powerValue

with open(input_file) as openfileobject:
    for line in openfileobject:
        cleanline = line.strip()
        gameData = cleanline.split(':')
        gameRounds = list(map(str.strip, gameData[1].split(';')))
        #print(gameRounds)
        powerSum = powerSum + checkGameRounds(gameRounds)

print(powerSum)