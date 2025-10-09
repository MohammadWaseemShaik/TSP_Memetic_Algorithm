import random
from utils import total_dis
from crossover import order_crossover
from mutation import swap_mutation

def ga_tsp(cities, pop_size=100, generations=100, mutation_rate=0.2):
    n = len(cities)
    population = [random.sample(range(n), n) for _ in range(pop_size)]
    best_lengths = []

    for _ in range(generations):
        fitness = [1 / total_dis(ind, cities) for ind in population]
        best_lengths.append(1 / max(fitness))

        def select():
            a, b = random.sample(range(pop_size), 2)
            return population[a] if fitness[a] > fitness[b] else population[b]

        new_pop = []
        for _ in range(pop_size):
            p1, p2 = select(), select()
            child = order_crossover(p1, p2)
            child = swap_mutation(child, mutation_rate)
            new_pop.append(child)
        population = new_pop

    best_ind = min(population, key=lambda ind: total_dis(ind, cities))
    return best_ind, total_dis(best_ind, cities), best_lengths