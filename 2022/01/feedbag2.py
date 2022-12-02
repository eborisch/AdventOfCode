#!/usr/bin/env python

import sys

reindeer = []

FOOD = 0

while y := sys.stdin.readline():
    y = y.strip()
    if y:
        FOOD += int(y)
    else:
        reindeer.append(FOOD)
        FOOD = 0

reindeer.sort()

print(sum(reindeer[-3:]))
