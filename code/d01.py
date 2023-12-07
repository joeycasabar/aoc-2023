#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    prog='Advent Of Code - Day 1',
    description="calculate calibration values"
)

parser.add_argument('input', type=open)

args = parser.parse_args()

count = 1


def find_numbers(line):
    print(f"-------- parsing line {count}: {line} --------")
    while any(substring in line for substring in replacements):
        # first, find the soonest digit to replace
        word_index = []
        for digit in range(1, 10, 1):
            word = replacements[digit]
            index = len(line)
            if word in line:
                index = line.index(word)
            word_index.append(index)
        new_num = 1 + word_index.index(min(word_index))
        word = replacements[new_num]
        print(f"replacing {word} with {new_num}")
        newline = line.replace(word, str(new_num))
        print(f"old: {line}, new: {newline}")
        line = newline

    # filter out only the digits
    return ''.join(filter(str.isdigit, line))


def replace_numbers(line):
    print(f"-------- parsing line {count}: {line} --------")
    for digit in range(1, 10, 1):
        word = replacements[digit]
        if word in line:
            new_string = word + str(digit) + word
            print(f"replacing {word} with {digit}")
            newline = line.replace(word, new_string)
            print(f"old: {line}, new: {newline}")
            line = newline

    # filter out only the digits
    return ''.join(filter(str.isdigit, line))


def parse_numbers(numbers):
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

replacements = ['zero', 'one', 'two', 'three',
                'four', 'five', 'six', 'seven', 'eight', 'nine']


# open the input file and read line by line
for line in args.input:
    # show the raw input for debugging purposes
    sum += parse_numbers(replace_numbers(line[:-1]))
    count += 1

# print the final sum
print(f"sum: {sum}")
