#!/usr/bin/env python

import sys

scores = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
score = 0

while y := sys.stdin.readline().strip():
    s = len(y)

    if not s:
        continue

    e = set(y[0:s//2]).intersection(set(y[s//2:]))

    score = score + scores.index(e.pop())

print(score)
