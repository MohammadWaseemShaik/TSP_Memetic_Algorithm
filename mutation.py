import random

def mutate(ind, mutation_rate=0.2):
    n = len(ind)
    if random.random() < mutation_rate:
        i, j = random.sample(range(n), 2)
        ind[i], ind[j] = ind[j], ind[i]
    return ind