#!/usr/bin/env python3

# make a variable to hold our final sum
sum = 0

# open the input file and read line by line
with open('./inputs/d01.txt', 'r') as input:
    for line in input:
        # show the raw input for debugging purposes
        print(line)
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
        # cum all of the calibration values
        sum += int(result)
        # print everything we found
        print(
            f"found digits: {numbers}, length: {length}, first: {first}, last: {last}, out: {result}")

# print the final sum
print(f"sum: {sum}")
