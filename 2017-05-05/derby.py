import random

# Result
# N=50000
# horses=20
#
# [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
#  0.0, 0.0, 0.0, 0.0, 0.0, 6e-05, 0.0001,
#  0.00124, 0.0103, 0.05642, 0.23584, 0.74076]
#

steps_to_win = 200
horses = 20
# make sure 500 + horses*p_increment < 1000
p_increment = 20

c = [0.0]*horses
N = 5000

for i in range(0, N):
    steps = [0]*horses
    while max(steps) < steps_to_win:
        for j in range(0, horses):
            if random.randint(0,1000) < 500 + p_increment * (j+1):
                steps[j] = steps[j] + 1
            else:
                steps[j] = steps[j] - 1
    for j in range(0, horses):
        if steps[j] >= steps_to_win:
            c[j] += 1

print map(lambda x: x/N, c)
