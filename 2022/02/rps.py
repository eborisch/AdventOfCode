#!/usr/bin/env python

import sys

smat = ((3,6,0),
        (0,3,6),
        (6,0,3))

def imap(abc):
    return ord(abc) - (ord('A') if abc in 'ABC' else ord('X'))

SCORE = 0

while y := sys.stdin.readline().strip():
    (A,B) = map(imap, y.split(' '))
    SCORE += smat[A][B] + B + 1

print(SCORE)
