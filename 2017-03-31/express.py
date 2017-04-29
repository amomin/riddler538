#!/bin/python

import random

c = 0
N = 10000000
for i in range(0,N):
    x = random.randint(0,60000000)
    y = random.randint(0,60000000)
    if abs(x-y) <= 15000000:
        c += 1

print c, N
print (7.0/16.0) * N
