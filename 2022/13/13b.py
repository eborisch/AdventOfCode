#!/usr/bin/env python

import sys

from collections import UserList

def comp(left, right):
    for l,r in zip(left,right):
        res = None
        if isinstance(l, int) and isinstance(r, int):
            if l != r:
                return l < r
        elif isinstance(l, int) and isinstance(r, list):
            res = comp([l], r)
        elif isinstance(l, list) and isinstance(r, int):
            res = comp(l, [r])
        else:
            res = comp(l, r)
        if res is not None:
            return res
    if len(left) < len(right):
        return True
    elif len(right) < len(left):
        return False
    return None

class customList(UserList):
    def __init__(self, liste):
        super().__init__(liste)
    def __lt__(self, right):
        return comp(self, right)

din = sys.stdin.readlines()
items = []
for n in din:
    if len(n) == 1:
        continue
    items.append(customList(eval(n.strip())))

KEYS = [customList([[2]]), customList([[6]])]

items.extend(KEYS)
items.sort()

print((items.index(KEYS[0]) + 1) * (items.index(KEYS[1]) + 1))
