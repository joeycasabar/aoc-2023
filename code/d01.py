#!/usr/bin/env python3

sum = 0

with open('./inputs/d01.txt', 'r') as input:
    for line in input:
        print(line)
        numbers = ''.join(filter(str.isdigit, line))
        first = numbers[0]
        length = len(numbers)
        if length > 1:
            last = numbers[-1]
        else:
            last = first
        result = first + last
        sum += int(result)
        print(f"found digits: {numbers}, length: {length}, first: {first}, last: {last}, out: {result}")

print(f"sum: {sum}")