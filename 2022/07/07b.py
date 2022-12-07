#!/usr/bin/env python

import sys
from collections import defaultdict

tree = {}
sizes = defaultdict(lambda : 0)

LOCATION = []

TOT = 70000000
GOAL = 30000000

def cd(c):
    if c == '/':
        LOCATION.clear()
    elif c == '..':
        LOCATION.pop()
    else:
        LOCATION.append(c)
    
while lin := sys.stdin.readline():
    # Can ignore 'ls' and 'dir' entries
    l = lin.strip().split(' ')
    if l[0] == '$':
        if l[1] == 'cd':
            cd(l[2])
        continue
    if l[0] != 'dir':
        loc = [''] + LOCATION[:]
        while loc:
            sizes['/'.join(loc)] += int(l[0])
            loc.pop()

x = list(sizes.values())
x.sort()

req = GOAL - (TOT - x[-1])

for v in x:
    if v >= req:
        print(v)
        break

