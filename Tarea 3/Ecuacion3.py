import pygad
import numpy as np

# Define la función objetivo
def equation3(x, i):
    return np.sin(x) * (np.sin((i * x**2) / np.pi))**20

# Define la función que calcula la suma de equation3 para una lista de valores
def solution3(d, x):
    total = 0
    for i in range(d):
        total += equation3(x[i], i + 1) * -1
    return total

# Define la función de aptitud que PyGAD utilizará para evaluar cada solución
def fitness_func(ga_instance, solution, solution_idx):
    d = len(solution)
    return -solution3(d, solution)

# Configuración del algoritmo genético
num_generations = 100  # Número de generaciones
num_parents_mating = 5  # Número de padres que se seleccionarán para reproducirse
sol_per_pop = 20  # Tamaño de la población
num_genes = 5
# Rango de los valores de las soluciones (genes)
gene_space = {'low': 0, 'high': np.pi}

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
