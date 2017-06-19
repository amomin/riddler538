import random

def simulate(N, p):
    print N, p
    count = 0.0
    for simulation_number in range(0, N):
        tags = [-1]*p
        while (len(filter(lambda x: x == -1, tags)) > 1):
            tagger = -1
            taggee = -1
            while tagger < 0:
                tagger = random.randint(0, p-1)
                if tags[tagger] >= 0:
                    tagger = -1
            while taggee < 0:
                taggee = random.randint(0, p-1)
                if tags[taggee] >= 0 or taggee == tagger:
                    taggee = -1
            tags = map(lambda x: -1 if x == taggee else x, tags)
            tags[taggee] = tagger
            count += 1
    
    print count / N

# N = 3 -> 3
# N = 4 -> 7
# N = 5 -> 15
# N = 6 -> 31
# N = 7 -> 62 (probably 63)
# Probably f(N) = 2^(N-1) - 1
def main():
    simulate(1000, 10)
    

if __name__ == '__main__':
    main()
