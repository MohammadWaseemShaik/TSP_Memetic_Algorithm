import numpy as np
from ga import ga_tsp
from utils import total_dis

def run_ga_exp(cities, runs=30):
    results, all_curves, best_tour = [], [], None

    for _ in range(runs):
        tour, best_len, curve = ga_tsp(cities)
        results.append(best_len)
        all_curves.append(curve)
        if best_tour is None or best_len < total_dis(best_tour, cities):
            best_tour = tour

    lengths = np.array(results)
    mean_curve = np.mean(all_curves, axis=0)
    std_curve = np.std(all_curves, axis=0)
    return best_tour, lengths, mean_curve, std_curve