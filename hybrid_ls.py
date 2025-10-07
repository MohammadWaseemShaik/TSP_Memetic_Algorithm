import random
from distance_fun import total_distance

def two_opt_once(tour, dist_matrix, attempts=10):
    best = tour[:]
    best_len = total_distance(best, dist_matrix)
    n = len(tour)
    for _ in range(attempts):
        i, j = sorted(random.sample(range(n), 2))
        if j - i <= 1:
            continue
        new_tour = best[:i] + best[i:j][::-1] + best[j:]
        new_len = total_distance(new_tour, dist_matrix)
        if new_len < best_len:
            return new_tour
    return best


def lin_kernighan_once(tour, dist_matrix, attempts=5):
    best = tour[:]
    best_len = total_distance(best, dist_matrix)
    n = len(tour)
    for _ in range(attempts):
        a, b, c = sorted(random.sample(range(n), 3))
        new_tour = best[:a] + best[a:b][::-1] + best[b:c][::-1] + best[c:]
        new_len = total_distance(new_tour, dist_matrix)
        if new_len < best_len:
            return new_tour
    return best


def hybrid_local_search(tour, dist_matrix, depth=2):
    improved = tour[:]
    for _ in range(depth):
        improved = two_opt_once(improved, dist_matrix)
        improved = lin_kernighan_once(improved, dist_matrix)
    return improved
