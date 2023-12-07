#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    prog='Advent Of Code - Day 1',
    description="calculate calibration values"
)

parser.add_argument('input')

args = parser.parse_args()

max_r = 12
max_g = 13
max_b = 14

sum = 0


def parse_game(line):
    input = line.split(':')
    game_number = int(''.join(filter(str.isdigit, input[0])))
    results = [s.strip() for s in input[1].split(';')]
    print(f"game: {game_number}, subsets: {len(results)}")
    # print(f"results: {results}")
    if check_max(convert_results(results)):
        return 0
    else:
        return game_number

# each game is a semicolon-separated string of subsets
# each subset is a comma-separated strong of number-color pairs


def check_max(subsets):
    print(f"checking game")
    fault = False
    for subset in subsets:
        if int(subset.get('red', 0)) > max_r or int(subset.get('green', 0)) > max_g or int(subset.get('blue', 0)) > max_b:
            print("max exceeded!")
            fault = True
            break
    return fault


def convert_results(results):
    print(f"extracting counts from {results}")
    subsets = []
    for subset in results:
        samples = dict((color, num) for num, color in [tuple(
            s.split(' ')) for s in [s.strip() for s in subset.split(',')]])
        subsets.append(samples)
    return subsets


with open(args.input) as input:
    for line in input:
        game = line.rstrip()
        sum += parse_game(game)
    print(f"total: {sum}")
