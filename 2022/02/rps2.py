#!/usr/bin/env python

import sys

scores = {'A': {'X':3, 'Y':6, 'Z':0},
          'B': {'X':0, 'Y':3, 'Z':6},
          'C': {'X':6, 'Y':0, 'Z':3}}

choice = {'X':1, 'Y':2, 'Z':3}

def reverse(a, score):
    for (p,s) in scores[a].items():
        if s == score:
            return p

select = {'X':lambda x: reverse(x, 0),
          'Y':lambda x: reverse(x, 3),
          'Z':lambda x: reverse(x, 6)}

SCORE = 0

while y := sys.stdin.readline():
    y = y.strip()
    if not y:
        continue
    (A,B) = y.split(' ')
    B = select[B](A)
    SCORE += scores[A][B] + choice[B]

print(SCORE)
