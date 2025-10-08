import random

def mutate_swap(ind, mutation_rate=0.2):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(ind)), 2)
        individual[i:j+1] = individual[i:j+1][::-1]
    return ind

