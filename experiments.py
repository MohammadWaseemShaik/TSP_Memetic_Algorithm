import time
import random
import numpy as np
from memetic_algo import memetic_tsp
from distance_fun import total_distance, create_distance_matrix

def pad_curves(curves):
    max_len = max(len(c) for c in curves)
    padded = [list(c) + [c[-1]] * (max_len - len(c)) for c in curves]
    return np.array(padded)

def run_ma_experiments(cities, runs=10, **ma_kwargs):
    results, all_curves, best_tour = [], [], None

    for r in range(runs):
        seed = int(time.time() * 1000) % 2**32
        random.seed(seed + r)
        np.random.seed((seed + r) % 2**32)

        start = time.time()
        tour, best_len, curve = memetic_tsp(cities, **ma_kwargs)
        runtime = time.time() - start

        results.append((best_len, runtime))
        all_curves.append(curve)
        if best_tour is None or best_len < total_distance(best_tour, create_distance_matrix(cities)):
            best_tour = tour

        print(f"Run {r+1}/{runs}: best_len={best_len:.2f}, time={runtime:.3f}s")

    lengths = np.array([res[0] for res in results])
    times = np.array([res[1] for res in results])

    curves_array = pad_curves(all_curves)
    mean_curve = np.mean(curves_array, axis=0)
    std_curve = np.std(curves_array, axis=0)

    return best_tour, lengths, times, mean_curve, std_curve
