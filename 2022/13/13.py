#!/usr/bin/env python

import sys
import re
import numpy as np

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
    elif len(left) > len(right):
        return False
    return None

din = sys.stdin.readlines()
score = 0
for n in range(0,len(din),3):
    left = eval(din[n].strip())
    right = eval(din[n+1].strip())
    
    if comp(left,right):
        score += n//3 + 1

print(score)


