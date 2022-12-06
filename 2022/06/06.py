#!/usr/bin/env python

import sys

dat = sys.stdin.read().strip()

queue = []

USIZE = 4 # or 14 for part 2

for n,d in enumerate(dat):
    queue.append(d)
    if len(set(queue)) == USIZE:
        break
    if len(queue) == USIZE:
        queue.pop(0)

print(n + 1)
