# Author: Kevin Johnson
# Created date: DEC 01 2023

# Advent of Code 2023
# DAY 01 PART 02

# 55929 too high
# Answer 55902

from sys import argv
import re

script, input_file = argv

calibrationValueSum = 0

def get_calibration_val(numlist):
    calib_val_str = ''
    if not numlist[0].isdigit():
        calib_val_str = calib_val_str + (str(convert_num_name(numlist[0])))
    else:
        calib_val_str =  calib_val_str + str(numlist[0])
    # did I stutter??
    if not numlist[-1].isdigit():
        calib_val_str = calib_val_str + (str(convert_num_name(numlist[-1])))
    else:
        calib_val_str =  calib_val_str + str(numlist[-1])

    return calib_val_str

def convert_num_name(num_name):
    digit = 0
    match num_name:
        case 'one':
            digit = 1
        case 'two':
            digit = 2
        case 'three':
            digit = 3
        case 'four':
            digit = 4
        case 'five':
            digit = 5
        case 'six':
            digit = 6
        case 'seven':
            digit = 7
        case 'eight':
            digit = 8
        case 'nine':
            digit = 9
        case 'zero':
            digit = 0
        case default:
            digit = 0
    return digit

with open(input_file) as openfileobject:
    for line in openfileobject:
        cleanline = line.strip()
        # positive lookahead FTW
        temp = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))', cleanline)
        calval = int(get_calibration_val(temp))
        calibrationValueSum = calibrationValueSum + calval

print(f"Calibration total is: {calibrationValueSum}")