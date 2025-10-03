import time
import numpy as np
from memetic_algo import memetic_tsp
from distance_fun import total_dis

def pad_curves(curves):
    """Pad all convergence curves to same length with last value."""
    max_len = max(len(c) for c in curves)
    padded = [c + [c[-1]] * (max_len - len(c)) for c in curves]
    return np.array(padded)

def run_ma_experiments(cities, runs=10):
    results, all_curves, best_tour = [], [], None

    for r in range(runs):
        start = time.time()
        tour, best_len, curve = memetic_tsp(cities)
        runtime = time.time() - start
        results.append((best_len, runtime))
        all_curves.append(curve)
        if best_tour is None or best_len < total_dis(best_tour, cities):
            best_tour = tour

    lengths = np.array([res[0] for res in results])
    times = np.array([res[1] for res in results])
    curves_array = pad_curves(all_curves)
    mean_curve = np.mean(curves_array, axis=0)
    std_curve = np.std(curves_array, axis=0)

    return best_tour, lengths, times, mean_curve, std_curve