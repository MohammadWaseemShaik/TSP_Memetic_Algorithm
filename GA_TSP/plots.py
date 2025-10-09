import os
import matplotlib.pyplot as plt
import numpy as np

def save_results_plot(best_tour, cities, lengths, mean_curve, std_curve, filename):
    os.makedirs("results", exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(12,8))
    fig.suptitle("Berlin52 - Genetic Algorithm", fontsize=14)

    # Best Route
    tour_cities = [cities[i] for i in best_tour] + [cities[best_tour[0]]]
    axes[0,0].plot([c[0] for c in tour_cities], [c[1] for c in tour_cities], marker='o')
    axes[0,0].set_title("Best Route")

    # Tour Lengths Distribution
    axes[0,1].hist(lengths, bins=10, edgecolor='black')
    axes[0,1].set_title("Tour Lengths Distribution")

    # Convergence Curve
    gens = range(len(mean_curve))
    axes[1,0].plot(gens, mean_curve, label="Mean Best Length")
    axes[1,0].fill_between(gens, mean_curve-std_curve, mean_curve+std_curve, alpha=0.2)
    axes[1,0].set_title("Convergence Curve")

    # Summary
    axes[1,1].axis("off")
    summary = (f"Runs: {len(lengths)}\n"
               f"Avg Length: {np.mean(lengths):.2f}\n"
               f"Best Length: {np.min(lengths):.2f}")
    axes[1,1].text(0.1,0.5, summary, fontsize=12)

    fig.savefig(f"results/{filename}.png")
    plt.close(fig)
    print(f"[INFO] Results saved as results/{filename}.png")