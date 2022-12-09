#!/usr/bin/env python

import sys
import numpy as np

def iarr(x):
    return np.array(x, dtype=int)

dirs = {'R': iarr(( 0, 1)),
        'L': iarr(( 0,-1)),
        'U': iarr(( 1, 0)),
        'D': iarr((-1, 0))}

steps = []
while l := sys.stdin.readline().strip():
    l = l.split()
    N = int(l[1])
    steps.extend(l[0] * N)

# The source of pain:
# hit = set((0,0)) # {0}, not {(0,0)}; DOH! Still got the right answer
# if (0,0) is never visited again
hit = set(((0,0),))

H = iarr((0,0))
T = iarr((0,0))

for s in steps:
    H = H + dirs[s]
    D = H - T

    if np.max(np.abs(D)) <= 1:
        continue

    D[D > 1] = 1
    D[D < -1] = -1
    T = T + D
    hit.add(tuple(T))

print(len(hit))
