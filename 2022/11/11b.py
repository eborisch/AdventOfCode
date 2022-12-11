#!/usr/bin/env python

import sys
import re
import numpy as np


class Monkey:
    MONKIES = []
    LCD = []

    def __init__(self, fdin):
        self.inspect = 0

        def l_ints():
            return list(map(int, re.findall(r'\d+', fdin.readline())))
        
        l = fdin.readline()

        # Monkey header
        if 'Monkey' not in l:
            raise Exception(f"error: Expected Monkey : [{l}]")
        
        # Starting Items
        self.items = l_ints()
        
        # Operation
        op,opval = fdin.readline().split()[4:6]
        # don't embed conditionals in lambda, select correct case at
        # construction
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
        test = l_ints()[0]
        Monkey.LCD.append(test)
        self.test = lambda x : not x % test

        # Dests choices[0] for test == false
        self.choices = l_ints()
        self.choices.insert(0,l_ints()[0])

        # Blank
        fdin.readline()
    
    def process(self):
        # In case we throw to ourselves..
        items = self.items[:]
        self.items.clear()
        for item in items:
            self.inspect += 1
            item = self.op(item) % Monkey.LCD
            dest = self.choices[self.test(item)]
            Monkey.MONKIES[dest].items.append(item)

    @staticmethod
    def load():
        try:
            while m := Monkey(sys.stdin):
                Monkey.MONKIES.append(m)
        except Exception as e:
            print("Found {} monkies.".format(len(Monkey.MONKIES)))
            #print(e)

        Monkey.LCD = np.lcm.reduce(Monkey.LCD)

    @staticmethod
    def score():
        l = [m.inspect for m in Monkey.MONKIES]
        l.sort()
        return l[-2] * l[-1]

Monkey.load()

for n in range(10000):
    for m in Monkey.MONKIES:
        m.process()

print(Monkey.score())
