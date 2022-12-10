#!/usr/bin/env python

import sys
import numpy as np

X = [1]
s = 0
while l := sys.stdin.readline().strip():
    l = l.split()
    if l[0] == 'noop':
        X.append(X[-1])
        continue
    d = int(l[1])
    X.append(X[-1])
    X.append(X[-1] + d)

print(sum(list(x[0] * x[1] for x in zip(X[19::40], range(20,230,40)))))

for beg in range(0,241):
    loc = beg % 40
    if beg and not loc:
        print()
    if abs(X[beg] - loc) <= 1:
        print("#", end='')
    else:
        print(".", end='')


