#!/usr/bin/env python

import sys
from collections import defaultdict

import numpy as np
d = sys.stdin.readlines()
N = len(d[0]) - 1
M = len(d)

dat = np.zeros((M,N), dtype=int)
flood_lr = np.zeros((M,N), dtype=int)
flood_rl = np.zeros((M,N), dtype=int)
flood_du = np.zeros((M,N), dtype=int)
flood_ud = np.zeros((M,N), dtype=int)

print(M)
print(N)
s = 0
for (m, lin) in enumerate(d):
    dat[m,:] = list(int(n) for n in lin.strip())
    flood_lr[m,:] = list(max(dat[m,0:n]) for n in range(1,N+1))
    flood_rl[m,:] = list(max(dat[m,n:]) for n in range(0,N))

for n in range(N):
    flood_ud[:,n] = list(max(dat[0:m,n]) for m in range(1,M+1))
    flood_du[:,n] = list(max(dat[m:,n]) for m in range(0,M))

lr = np.max(dat, 1)
ud = np.max(dat, 0)
cat = np.concatenate

flood_lr = (np.diff(flood_lr,axis=1, prepend=-1))
flood_rl = (np.fliplr(np.diff(np.fliplr(flood_rl),axis=1, prepend=-1)))
flood_ud =(np.diff(flood_ud,axis=0, prepend=-1))
flood_du = (np.flipud(np.diff(np.flipud(flood_du),axis=0, prepend=-1)))

res = (flood_lr > 0) | (flood_rl > 0) | (flood_ud > 0) | (flood_du > 0)

print(np.sum(res))

