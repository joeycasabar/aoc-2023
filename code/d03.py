#!/usr/bin/env python3

import argparse
symbols = "#$%&*+-/=@"
numbers = "0123456789"

parser = argparse.ArgumentParser(
    prog='Advent Of Code - Day 3',
    description="Gear Ratios"
)

parser.add_argument('input')

args = parser.parse_args()


def get_locations(map, charset):
    locations = []
    for c in charset:
        height = len(map[0])
        for y in range(0, height, 1):
            row = map[y]
            if c in row:
                x = row.index(c)
                locations.append(
                    {
                        'symbol': c,
                        'x': x + 1,
                        'y': y + 1
                    }
                )
    return locations


with open(args.input) as input:
    map = []
    for line in input:
        map.append(line.rstrip())
    # print(map)
    symbols_xy = get_locations(map, symbols)
    print(symbols_xy)
    numbers_xy = get_locations(map, numbers)
    print(numbers_xy)
