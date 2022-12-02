#!/usr/bin/env python

import sys

scores = {'A': {'X':3, 'Y':6, 'Z':0},
          'B': {'X':0, 'Y':3, 'Z':6},
          'C': {'X':6, 'Y':0, 'Z':3}}

choice = {'X':1, 'Y':2, 'Z':3}

SCORE = 0

while y := sys.stdin.readline():
    y = y.strip()
    if not y:
        continue
    (A,B) = y.split(' ')
    SCORE += scores[A][B] + choice[B]

print(SCORE)
