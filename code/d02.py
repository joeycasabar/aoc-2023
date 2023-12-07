#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    prog='Advent Of Code - Day 2',
    description="Cube Conundrum"
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
    return get_min_power(convert_results(results))
    # print(f"results: {results}")
    # if check_max(convert_results(results)):
    #     return 0
    # else:
    #     return game_number

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


def get_min_power(subsets):
    print(subsets)
    min_r = 0
    min_g = 0
    min_b = 0
    for s in subsets:
        if s.get('red', 0) > min_r:
            min_r = s['red']
        if s.get('green', 0) > min_g:
            min_g = s['green']
        if s.get('blue', 0) > min_b:
            min_b = s['blue']
    print(f"min_r: {min_r}, min_g: {min_g}, min_b: {min_b}")
    return min_r * min_g * min_b


def convert_results(results):
    print(f"extracting counts from {results}")
    subsets = []
    for subset in results:
        samples = dict((color, int(num)) for num, color in [tuple(
            s.split(' ')) for s in [s.strip() for s in subset.split(',')]])
        subsets.append(samples)
    return subsets


with open(args.input) as input:
    for line in input:
        game = line.rstrip()
        sum += parse_game(game)
    print(f"total: {sum}")
