#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    prog='Advent Of Code - Day 3',
    description="Gear Ratios"
)

parser.add_argument('input')

args = parser.parse_args()

with open(args.input) as input:
    for line in input:
        print(line.rstrip())
