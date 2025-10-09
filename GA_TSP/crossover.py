import random

def order_crossover(p1, p2):
    n = len(p1)
    start, end = sorted(random.sample(range(n), 2))
    child = [None]*n
    child[start:end] = p1[start:end]
    pos = end
    for gene in p2:
        if gene not in child:
            if pos >= n: pos = 0
            child[pos] = gene
            pos += 1
    return child
