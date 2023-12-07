#!/usr/bin/env python3


count = 1


def find_numbers(line):
    print(f"parsing line {count}: {line}")
    for digit, word in replacements:
        if word in line:
            print(f"replacing {word} with {digit}")
            newline = line.replace(word, str(digit))
            print(f"old: {line}, new: {newline}")
            line = newline

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

replacements = [
    (1, 'one'),
    (2, 'two'),
    (3, 'three'),
    (4, 'four'),
    (5, 'five'),
    (6, 'six'),
    (7, 'seven'),
    (8, 'eight'),
    (9, 'nine')
]


# open the input file and read line by line
with open('./inputs/d01.txt', 'r') as input:
    for line in input:
        # show the raw input for debugging purposes
        sum += find_numbers(line)
        count += 1

# print the final sum
print(f"sum: {sum}")
