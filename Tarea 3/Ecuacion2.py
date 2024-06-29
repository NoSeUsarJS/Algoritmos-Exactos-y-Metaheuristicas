import pygad
import numpy as np

# Define la función objetivo
def equation2(x1, x2):
    return 100 * ((x2 - x1**2)**2) + (x1 - 1)**2

# Define la función que calcula la suma de equation2 para una lista de valores
def solution2(d, x):
    total = 0
    for i in range(d - 1):
        total += equation2(x[i], x[i + 1])
    return total

# Define la función de aptitud que PyGAD utilizará para evaluar cada solución
def fitness_func(ga_instance, solution, solution_idx):
    d = len(solution)
    return -solution2(d, solution)



# Configuración del algoritmo genético
num_generations = 100
num_parents_mating = 1
sol_per_pop = 400  
num_genes = 20 # d
gene_space = {'low': -30, 'high': 30}

# Creación de una instancia de la clase pygad.GA
ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    gene_space=gene_space
)

# Ejecutar el algoritmo genético
ga_instance.run()

# Obtener la mejor solución
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Mejor solución: ", solution)
print("Fitness de la mejor solución: ", solution_fitness)
print("Valor de la función objetivo para la mejor solución: ", -solution_fitness)  # Negamos porque nuestra función de aptitud era negativa
