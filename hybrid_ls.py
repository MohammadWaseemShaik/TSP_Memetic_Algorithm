import random
from distance_fun import total_dis

def two_opt_once(tour, cities):
    best = tour[:]
    best_dist = total_dis(best, cities)
    n = len(tour)
    for _ in range(10):
        i, j = sorted(random.sample(range(n), 2))
        if j - i <= 1:
            continue
        new_tour = best[:i] + best[i:j][::-1] + best[j:]
        new_dist = total_dis(new_tour, cities)
        if new_dist < best_dist:
            return new_tour
    return best

def lin_kernighan_once(tour, cities):
    n = len(tour)
    best = tour[:]
    best_dist = total_dis(best, cities)
    for _ in range(5):
        a, b, c = sorted(random.sample(range(n), 3))
        new_tour = best[:a] + best[a:b][::-1] + best[b:c][::-1] + best[c:]
        new_dist = total_dis(new_tour, cities)
        if new_dist < best_dist:
            return new_tour
    return best

def hybrid_local_search(tour, cities):
    improved = tour[:]
    for _ in range(3):
        improved = two_opt_once(improved, cities)
        improved = lin_kernighan_once(improved, cities)
    return improved