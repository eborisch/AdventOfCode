#!/usr/bin/env python

import sys

scores = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
score = 0
idx = 0

while y := sys.stdin.readline().strip():
    if not y:
        continue

    y = set(y)
    e = y if idx == 0 else e.intersection(y)

    idx += 1
    if idx < 3:
        continue
    idx = 0

    score = score + scores.index(e.pop())

print(score)
