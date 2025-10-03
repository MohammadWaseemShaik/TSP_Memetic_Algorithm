import os
import matplotlib.pyplot as plt
import numpy as np

def save_results(cities, best_tour, lengths, times, mean_curve, std_curve, dataset_name="Berlin52", optimum=None):
    os.makedirs("results", exist_ok=True)

    fig, axes = plt.subplots(2, 2, figsize=(12,8))
    fig.suptitle(f"TSP - Memetic Algorithm ({dataset_name})", fontsize=14)

    # Best route
    tour_cities = [cities[i] for i in best_tour] + [cities[best_tour[0]]]
    axes[0,0].plot([c[0] for c in tour_cities], [c[1] for c in tour_cities], marker='o')
    axes[0,0].set_title("Best Route")

    # Runtime
    axes[0,1].hist(times, bins=10, edgecolor='black')
    axes[0,1].set_title("Runtime Distribution")

    # Convergence
    gens = np.arange(len(mean_curve))
    axes[1,0].plot(gens, mean_curve, label="Mean Best Length")
    axes[1,0].fill_between(gens, mean_curve-std_curve, mean_curve+std_curve, alpha=0.2)
    axes[1,0].set_title("Convergence Curve")
    axes[1,0].legend()

    # Summary
    axes[1,1].axis("off")
    avg_len = np.mean(lengths); best_len = np.min(lengths); avg_time = np.mean(times)
    summary = f"Runs: {len(lengths)}\nAvg Length: {avg_len:.2f}\nBest Length: {best_len:.2f}\nAvg Runtime: {avg_time:.3f}s"
    if optimum:
        error = (best_len - optimum) / optimum * 100
        summary += f"\nKnown Optimum: {optimum}\nError: {error:.2f}%"
    axes[1,1].text(0.1,0.5, summary, fontsize=12)

    plt.tight_layout()
    plt.savefig(f"results/{dataset_name}_results.png")
    plt.close(fig)
    print(f"Results saved to results/{dataset_name}_results.png")