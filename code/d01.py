#!/usr/bin/env python3

def find_numbers(line):
    print(line)
    if any(substring in line for substring in words):
        print("found words")
    # filter out only the digits
    numbers = ''.join(filter(str.isdigit, line))
    # get the first digit in the list of digits
    first = numbers[0]
    # see how many digits were detected
    length = len(numbers)
    # reuse the same digit if there is only one, otherwise use the last digit
    if length > 1:
        last = numbers[-1]
    else:
        last = first
    # make the new number from the first and last digits
    result = first + last
    # print everything we found
    print(
        f"found digits: {numbers}, length: {length}, first: {first}, last: {last}, out: {result}")
    # return the calibration values
    return int(result)


# make a variable to hold our final sum
sum = 0

words = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]


# open the input file and read line by line
with open('./inputs/d01.txt', 'r') as input:
    for line in input:
        # show the raw input for debugging purposes
        sum += find_numbers(line)

# print the final sum
print(f"sum: {sum}")
