import numpy as np

def create_distance_matrix(cities):
    arr = np.asarray(cities)
    diff = arr[:, None, :] - arr[None, :, :]
    dist_mat = np.sqrt((diff ** 2).sum(axis=2))
    return dist_mat

def total_distance(tour, dist_matrix):
    total = 0.0
    n = len(tour)
    for i in range(n):
        total += dist_matrix[tour[i], tour[(i + 1) % n]]
    return total
