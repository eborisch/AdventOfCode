#!/usr/bin/env python

import sys
import re

pat = re.compile(r'(\[(.)\]|   ) ?')
move = re.compile(r'move (\d+) from (\d+) to (\d+)')

dat = sys.stdin.readlines()
blank = dat.index('\n')

crates = dat[:blank-1]
moves = dat[blank+1:]

towers = [[] for n in range(len(crates[0])//4)]

for y in crates:
    t = [x[1] for x in pat.findall(y)]
    for (twr, c) in zip(towers, t):
        if c:
            twr.insert(0,c)

for y in moves:
    x = move.match(y)
    if not x:
        break

    count, src, dst = map(int, x.groups())
    src -= 1
    dst -= 1

    towers[dst].extend(towers[src][-count:])
    towers[src] = towers[src][:-count]

for twr in towers:
    print(twr.pop(), end='')

print()
