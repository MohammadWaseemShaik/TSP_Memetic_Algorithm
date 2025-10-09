import numpy as np

def eu_dis(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def total_dis(tour, cities):
    return sum(eu_dis(cities[tour[i]], cities[tour[(i+1)%len(tour)]])
               for i in range(len(tour)))
