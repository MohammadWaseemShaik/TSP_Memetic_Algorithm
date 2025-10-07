import os
import matplotlib.pyplot as plt
import numpy as np
from distance_fun import total_distance, create_distance_matrix

def save_results(cities, best_tour, lengths, times, mean_curve, std_curve, dataset_name="Berlin52", optimum=None):
    os.makedirs("results", exist_ok=True)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(f"TSP - Memetic Algorithm ({dataset_name})", fontsize=14)

    # Best route visualization
    route = [cities[i] for i in best_tour] + [cities[best_tour[0]]]
    axes[0, 0].plot([c[0] for c in route], [c[1] for c in route], marker='o')
    axes[0, 0].set_title("Best Route")

    # Runtime histogram
    axes[0, 1].hist(times, bins=10, edgecolor='black')
    axes[0, 1].set_title("Runtime Distribution")

    # Convergence curve
    gens = np.arange(len(mean_curve))
    axes[1, 0].plot(gens, mean_curve, label="Mean Length")
    axes[1, 0].fill_between(gens, mean_curve - std_curve, mean_curve + std_curve, alpha=0.2)
    axes[1, 0].set_title("Convergence Curve")
    axes[1, 0].legend()

    # Summary text
    axes[1, 1].axis("off")
    summary = f"Runs: {len(lengths)}\nAvg Len: {np.mean(lengths):.2f}\nBest: {np.min(lengths):.2f}\nAvg Time: {np.mean(times):.3f}s"
    if optimum:
        err = (np.min(lengths) - optimum) / optimum * 100
        summary += f"\nOptimum: {optimum}\nError: {err:.2f}%"
    axes[1, 1].text(0.1, 0.5, summary, fontsize=12)

    out_path = f"results/{dataset_name}_results.png"
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close(fig)
    print(f"Saved plot {out_path}")
