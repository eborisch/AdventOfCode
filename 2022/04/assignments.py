#!/usr/bin/env python

import sys
import re

pat = re.compile('\d+')

score = 0
score2 = 0

while y := sys.stdin.readline():
    v = list(map(int, pat.findall(y)))

    a = set(range(v[0], v[1]+1))
    b = set(range(v[2], v[3]+1))

    if a.union(b) in (a,b):
        score += 1
    if a.intersection(b):
        score2 += 1

print(score)
print(score2)
