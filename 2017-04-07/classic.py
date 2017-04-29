#!/bin/python

import sets

def classic(filled, prt):
    count = 0
    total = 0.0
    mp = {}
    unfilled = 0
    for x in filled:
        if x == None:
            unfilled += 1
    for x in range(0,10):
        if x in filled: continue
        MAX = 99999
        bestpos = 5
        bestexp = MAX
        for i in range(0, 4):
            if (filled[i] != None): continue
            filled[i] = x
            e = classic(filled, False)
            if e < bestexp:
                bestexp = e
                bestpos = i
            filled[i] = None
        if bestpos != 5:
            mp[x] = bestpos
            #print "Given", filled, "drawing", x, "should go in position", bestpos
            #print "expected product is", bestexp
            total += bestexp
            count += 1
        else:
            # Full
            return (10*filled[0] + filled[1]) * (10*filled[2] + filled[3])
    if prt and unfilled > 1:
        for k in mp:
            filled[mp[k]] = k
            classic(filled, True)
            filled[mp[k]] = None
            print "Given", filled, "drawing", k, "should go in position", mp[k]
        
    return total / count

def randomly1():
    total = 0.0
    count = 0.0
    for x in range(0,10):
        for y in range(0,10):
            if y == x: continue
            for w in range(0,10):
                if w == x: continue
                if w == y: continue
                for z in range(0,10):
                    if z == x: continue
                    if z == y: continue
                    if z == w: continue
                    count += 1
                    total += (10*x+y)*(10*w+z)
    return total/count

def r2(filled):
    total = 0.0
    count = 0.0
    for x in range(0,10):
        for i in range(0,4):
            if filled[i] != None: continue
            filled[i] = x
            t, c = r2(filled)
            total += t
            count += c
            filled[i] = None
    if count == 0:
        return (10*filled[0] + filled[1]) * (10*filled[2] + filled[3]), 1
    return total, count

print classic([None, None, None, None], True)
print randomly1()
t, c = r2([None,None,None,None])
print t/c
