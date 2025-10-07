import numpy as np
from datasets import load_berlin52
from experiments import run_ma_experiments
from plots import save_results

if __name__ == "__main__":
    cities, optimum = load_berlin52()

    best_tour, lengths, times, mean_curve, std_curve = run_ma_experiments(
        cities,
        runs=30,
        pop_size=100,
        generations=500,
        mutation_rate=0.1,
        local_search_prob=0.2,
        elite_fraction=0.3 ,
        randomness_in_gx=3
    )

    print("\n=== Summary ===")
    print(f"Runs: {len(lengths)}")
    print(f"Avg Length: {np.mean(lengths):.2f}")
    print(f"Best Length: {np.min(lengths):.2f}")
    print(f"Avg Runtime: {np.mean(times):.3f}s")

    if optimum:
        error = (np.min(lengths) - optimum) / optimum * 100
        print(f"Optimum: {optimum}, Error: {error:.2f}%")

    save_results(cities, best_tour, lengths, times, mean_curve, std_curve, dataset_name="Berlin52", optimum=optimum)
