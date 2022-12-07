#!/usr/bin/env python

import sys
from collections import defaultdict

sizes = defaultdict(lambda : 0)

LOCATION = []

def cd(c):
    if c == '/':
        LOCATION.clear()
    elif c == '..':
        LOCATION.pop()
    else:
        LOCATION.append(c)
    
while lin := sys.stdin.readline().strip():
    # Can ignore 'ls' and 'dir' entries
    l = lin.split(' ')
    if l[0] == '$':
        if l[1] == 'cd':
            cd(l[2])
        continue
    if l[0] != 'dir':
        loc = [''] + LOCATION[:]
        while loc:
            sizes['/'.join(loc)] += int(l[0])
            loc.pop()

s = 0
for v in sizes.values():
    if v <= 100000:
        s += v

print(s)

