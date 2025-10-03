import random, time
import numpy as np
from distance_fun import total_dis
from greedy_crossover import greedy_crossover
from mutation import mutate
from hybrid_ls import hybrid_local_search

def memetic_tsp(cities, pop_size=80, generations=60, mutation_rate=0.2):
    n = len(cities)
    population = [random.sample(range(n), n) for _ in range(pop_size)]
    best_lengths = []

    for gen in range(generations):
        fitness = [1 / total_dis(ind, cities) for ind in population]
        best_lengths.append(1 / max(fitness))

        def select():
            a, b = random.sample(range(pop_size), 2)
            return population[a] if fitness[a] > fitness[b] else population[b]

        new_pop = []
        for _ in range(pop_size):
            p1, p2 = select(), select()
            child = greedy_crossover(p1, p2, cities)
            child = mutate(child, mutation_rate)
            child = hybrid_local_search(child, cities)
            new_pop.append(child)
        population = new_pop

    best_ind = min(population, key=lambda ind: total_dis(ind, cities))
    return best_ind, total_dis(best_ind, cities), best_lengths