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

def simulation(balls, N_runs, debug=False):
    total = 0.0
    for i in range(0,N_runs):
        initial_balls = list(balls)
        c = play(initial_balls, debug)
        total += c
    return total / N_runs

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

def balls_from_partition(partition):
    i = 0
    balls = []
    for p in partition:
        for j in range(0, p):
            balls.append(i)
        i += 1
    return balls

def partitions(n):
    return partitions_up_to(n, n)

def partitions_up_to(n, max_p):
    if max_p > n: return partitions_up_to(n, n)
    results = []
    if max_p >= n: results = [[n]]
    for i in range(max_p, 0, -1):
        remaining = n - i
        new_max_p = min(max_p, min(i, n-i))
        if new_max_p < 1: continue
        sub_results = map(lambda(x): [i] + x, partitions_up_to(remaining, new_max_p))
        results += sub_results
    return results
        

#print partitions(2)
#print partitions(3)
#print partitions(4)
#print partitions(5)
#print partitions(6)

def simulate_all_partitions_of(n, N_runs):
    for p in partitions(n):
        ball_distribution = balls_from_partition(p)
        debug=False
        turns = simulation(ball_distribution, N_runs, debug)
        print ball_distribution, p, "->", turns

def simulate_two_colors_with_n_balls(N, N_runs):
    for i in range(0,N):
        if i > N/2: break
        p = [i,N-i]
        ball_distribution = balls_from_partition(p)
        debug=False
        turns = simulation(ball_distribution, N_runs, debug)
        print ball_distribution, p, "->", turns

def simulate_all_red_but_one_up_to(from_, to_, N_runs):
    for i in range(from_, to_ + 1):
        p = [i,1]
        ball_distribution = balls_from_partition(p)
        debug=False
        turns = simulation(ball_distribution, N_runs, debug)
        print ball_distribution, p, "->", turns

simulate_all_partitions_of(8, 500000)
#simulate_two_colors_with_n_balls(6, 100000)
#simulate_all_red_but_one_up_to(5, 5, 10000000)
