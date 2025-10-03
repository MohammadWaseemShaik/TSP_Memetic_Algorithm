import random
from distance_fun import euclidean_distance

def greedy_crossover(p1, p2, cities):
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
            next_city = min(candidates, key=lambda c: euclidean_distance(cities[current], cities[c]))
        else:
            next_city = min(remaining, key=lambda c: euclidean_distance(cities[current], cities[c]))

        child.append(next_city)
        remaining.remove(next_city)
        current = next_city

    return child