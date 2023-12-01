# Author: Kevin Johnson
# Created date: DEC 01 2023

# Advent of Code 2023
# DAY 01 PART 01

# 736824 too high
# 10196 too low
# Answer 56465

from sys import argv
import re

script, input_file = argv

calibrationValueSum = 0

with open(input_file) as openfileobject:
    for line in openfileobject:
        cleanline = line.strip()
        temp = re.findall(r'\d', cleanline)
        numberList = list(map(int, temp))
        concat = int(str(numberList[0]) + str(numberList[-1]))
        calibrationValueSum = calibrationValueSum + concat
        
print(f"Calibration total is: {calibrationValueSum}")