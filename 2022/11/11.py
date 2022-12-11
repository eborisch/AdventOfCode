#!/usr/bin/env python

import sys
import re
import numpy as np


class Monkey:
    MONKIES = []

    def __init__(self, fdin):
        self.inspect = 0

        def nline():
            return fdin.readline().split()
        
        l = fdin.readline()

        # Monkey header
        if 'Monkey' not in l:
            raise Exception(f"error: Expected Monkey : {l}")
        # Starting Items
        l = fdin.readline()
        self.items = list(map(int, re.findall(r'\d+', l)))
        # Operation
        op,opval = nline()[4:6]
        if opval != 'old':
            if op == '*':
                self.op = lambda x : x * int(opval)
            else:
                self.op = lambda x : x + int(opval)
        else:
            if op == '*':
                self.op = lambda x : x * x
            else:
                self.op = lambda x : x + x
        # Test
        test = int(fdin.readline().split()[3])
        self.test = lambda x : not x % test

        # Dests choices[0] for test == false
        self.choices = [int(nline()[5])]
        self.choices.insert(0,int(nline()[5]))

        # Blank
        fdin.readline()

    def process(self):
        items = self.items[:]
        self.items = []
        for it in items:
            self.inspect += 1
            it = self.op(it)
            it = it // 3
            dest = self.choices[self.test(it)]
            Monkey.MONKIES[dest].items.append(it)
try:
    while m := Monkey(sys.stdin):
        Monkey.MONKIES.append(m)
except:
    print("Found {} monkies.".format(len(Monkey.MONKIES)))

for n in range(20):
    for m in Monkey.MONKIES:
        m.process()

l = [m.inspect for m in Monkey.MONKIES]
l.sort()

print(l[-2] * l[-1])

