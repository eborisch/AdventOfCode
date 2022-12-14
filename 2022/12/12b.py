#!/usr/bin/env python

import sys
import re
import numpy as np

def printmap(x):
    for m in range(x.shape[0]):
        for n in range(x.shape[1]):
            if x[m,n] > 0:
                v='+'
            elif x[m,n]:
                v='o'
            else:
                v='.'
            print(v,end='')
        print()

din = sys.stdin.readlines()

M = len(din)
N = len(din[0].strip())

surf = np.zeros((M,N), dtype=int)
reached = np.zeros((M,N), dtype=int)

START = None
END = None

for m,d in enumerate(din):
    surf[m,:] = [ord(c) - ord('a') for c in d.strip()]

START = tuple(_[0] for _ in np.where(surf == (ord('S') - ord('a'))))
END = tuple(_[0] for _ in np.where(surf == (ord('E') - ord('a'))))

reached[surf == 0] = 1
reached[END] = -1
surf[START] = 0
surf[END] = ord('z') - ord('a')

def addoff(a, b):
    return tuple(sum(e) for e in zip(a,b))

spts = []
epts = [END]

dist = 0

step = 0

np.set_printoptions(threshold=sys.maxsize)


while not dist and (spts or epts):
    plist = epts
    last = plist[:]
    plist.clear()
    for p in last:
        if dist:
            break
        src = reached[p]
        l = surf[p]
        for d in ((-1,0),(1,0),(0,-1),(0,1)):
            p_ = addoff(p, d)
            if min(p_) < 0 or p_[0] >= M or p_[1] >= N:
                continue
            if src > 0 and surf[p_] - l > 1 or src < 0 and l - surf[p_] > 1:
                continue
            if reached[p_]:
                if reached[p_] != src:
                    dist = step + 1
                    break
            else:
                reached[p_] = src
                plist.append(p_)
    step += 1
    #printmap(reached)

print(dist)

