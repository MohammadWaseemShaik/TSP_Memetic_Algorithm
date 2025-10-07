import random
import numpy as np

from distance_fun import create_distance_matrix, total_distance
from greedy_crossover import greedy_crossover_stochastic
from mutation import mutate_swap
from hybrid_ls import hybrid_local_search

def roulette_select(population, fitness_vals):
    probs = fitness_vals / np.sum(fitness_vals)
    idx = np.random.choice(len(population), p=probs)
    return population[idx]

def initialize_population(n, pop_size):
    return [random.sample(range(n), n) for _ in range(pop_size)]

def memetic_tsp(cities, pop_size=80, generations=150, mutation_rate=0.02,
                local_search_prob=0.2, elite_fraction=0.3, randomness_in_gx=1):

    n = len(cities)
    dist_matrix = create_distance_matrix(cities)
    population = initialize_population(n, pop_size)

    best_lengths = []

    for gen in range(generations):
        lengths = np.array([total_distance(ind, dist_matrix) for ind in population])
        best_len = lengths.min()
        best_lengths.append(best_len)

        fitness = 1.0 / (lengths + 1e-12)
        elite_size = max(1, int(elite_fraction * pop_size))
        elite_indices = lengths.argsort()[:elite_size]
        elite = [population[i] for i in elite_indices]

        new_pop = []
        while len(new_pop) < pop_size - elite_size:
            p1 = roulette_select(population, fitness)
            p2 = roulette_select(population, fitness)
            child = greedy_crossover_stochastic(p1, p2, dist_matrix, randomness=randomness_in_gx)
            child = mutate_swap(child, mutation_rate)
            if random.random() < local_search_prob:
                child = hybrid_local_search(child, dist_matrix, depth=1)
            new_pop.append(child)

        survivors = []
        if len(new_pop) + elite_size < pop_size:
            survivors = [random.choice(population) for _ in range(pop_size - len(new_pop) - elite_size)]

        population = elite + new_pop + survivors
        population = population[:pop_size]

    final_lengths = [total_distance(ind, dist_matrix) for ind in population]
    best_idx = int(np.argmin(final_lengths))
    return population[best_idx], final_lengths[best_idx], best_lengths
