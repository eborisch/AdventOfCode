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

hit = set(((0,0),))

SEG = 10
H = np.zeros((2, SEG), dtype=int)

for s in steps:
    H[:,0] = H[:,0] + dirs[s]
    for n in range(1,SEG):
        D = H[:,n-1] - H[:,n]
        if np.max(np.abs(D)) <= 1:
            break # No need to update the rest of the rope
        D[D > 1] = 1
        D[D < -1] = -1
        H[:,n] = H[:,n] + D
        if n == SEG - 1:
            hit.add(tuple(H[:,-1]))

print(len(hit))
