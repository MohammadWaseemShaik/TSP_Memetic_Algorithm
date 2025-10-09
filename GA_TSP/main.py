from datasets import load_berlin52
from experiments import run_ga_exp
from plots import save_results_plot

if __name__ == "__main__":
    cities, optimum = load_berlin52()
    best_tour, lengths, mean_curve, std_curve = run_ga_exp(cities, runs=10)
    save_results_plot(best_tour, cities, lengths, mean_curve, std_curve, filename="Berlin52_GA")