import random
import numpy as np

def greedy_crossover_stochastic(p1, p2, dist_matrix, randomness=2):
    n = len(p1)
    remaining = set(p1)
    current = random.choice(p1)
    child = [current]
    remaining.remove(current)

    while remaining:
        candidates = []
        for parent in (p1, p2):
            idx = parent.index(current)
            left = parent[idx - 1]
            right = parent[(idx + 1) % n]
            candidates.extend([left, right])
        candidates = [c for c in candidates if c in remaining]

        if candidates:
            unique = list(dict.fromkeys(candidates))
            sorted_candidates = sorted(unique, key=lambda c: dist_matrix[current, c])
            k = min(randomness, len(sorted_candidates))
            next_city = random.choice(sorted_candidates[:k])
        else:
            next_city = min(list(remaining), key=lambda c: dist_matrix[current, c])

        child.append(next_city)
        remaining.remove(next_city)
        current = next_city

    return child
