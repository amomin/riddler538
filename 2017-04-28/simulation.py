import random

def different(balls):
    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i] != balls[j]: return True
    return False

def play(balls, debug=False):
    c = 0
    n = len(balls)
    while different(balls):
        b1 = 0
        b2 = 0
        while b1 == b2:
            b1 = random.randint(0, n-1)
            b2 = random.randint(0, n-1)
        balls[b1] = balls[b2]
        if debug:
            print balls
        c += 1
    return c

def simulation(n_balls, N_runs, debug=False):
    total = 0.0
    for i in range(0,N_runs):
        balls = range(0,n_balls)
        c = play(balls, debug)
        total += c
    print total / N_runs

def state(balls):
    x = [0]*4
    for b in balls:
        x[b] += 1
    if max(x) == 2:
        if 1 in x:
            #B
            return 0 
        #C
        return 1
    if max(x) == 3:
        #D
        return 2
    #E
    return 3

# Use to verify the transition matrix
# 1/2  1/6  1/3  0
# 0    1/3  2/3  0
# 0    1/4  1/2  1/4
# 0    0    0    1/1
def transitions():
    N = 100000
    m = [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,1.0]]
    for i in range(0,N):
        # B
        balls = [0, 1, 2, 2]
        while different(balls):
            s1 = state(balls)
            b1 = 0
            b2 = 0
            while b1 == b2:
                b1 = random.randint(0, 3)
                b2 = random.randint(0, 3)
            balls[b1] = balls[b2]
            s2 = state(balls)
            m[s1][s2] += 1
    for row in m:
        s = sum(row)
        print map(lambda(y): y/s, row)

n_balls = 4
N_runs = 50000
debug=False
simulation(n_balls, N_runs, debug)
