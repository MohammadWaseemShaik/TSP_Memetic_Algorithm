from datasets import load_berlin52
from experiments import run_ma_experiments
from plots import save_results

if __name__ == "__main__":
    cities, optimum = load_berlin52()
    best_tour, lengths, times, mean_curve, std_curve = run_ma_experiments(cities, runs=5)
    save_results(cities, best_tour, lengths, times, mean_curve, std_curve, dataset_name="Berlin52", optimum=optimum)
