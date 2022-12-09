#!/usr/bin/env python

import sys
from collections import defaultdict

import numpy as np
d = sys.stdin.readlines()
N = len(d[0]) - 1
M = len(d)

dat = np.zeros((M,N), dtype=int)

s = 0
for (m, lin) in enumerate(d):
    dat[m,:] = list(int(n) for n in lin.strip())

scores = np.zeros_like(dat)

for m in range(1,M-1):
    for n in range(1,N-1):
        base_loc = (m,n)
        h = dat[base_loc]
        s = 1
        for step in ((-1,0), (1,0), (0,-1), (0,1)):
            d = 1
            pos = tuple(base_loc[x]+step[x]*d for x in range(2))
            while pos[0] in range(0,M) and pos[1] in range(0,N):
                if dat[pos] >= h:
                    s = s * d
                    break
                d = d + 1
                pos = tuple(base_loc[x]+step[x]*d for x in range(2))
            else:
                s = s * (d - 1)
            
        scores[base_loc] = s
print(np.max(scores))
