import pygad
import numpy as np

# Define la función objetivo
def equation1(X):
    return (X**2) - 10 * np.cos(2 * np.pi * X) + 10

# Define la función de aptitud que PyGAD utilizará para evaluar cada solución
def fitness_func(ga_instance, solution, solution_idx):
    return -np.sum([equation1(x) for x in solution])

# Configuración del algoritmo genético
num_generations = 400  # Número de generaciones (Parametro)
num_parents_mating = 1  # Número de padres que se seleccionarán para reproducirse (Parametro)
sol_per_pop = 200  # Tamaño de la población (Parametro)
num_genes = 10  # Número de genes en cada solución (d)
gene_space = {'low': -5.12, 'high': 5.12} # Rango de los valores de las soluciones (genes)

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
print("Suma de la mejor solución: ", -solution_fitness)  # Negamos porque nuestra función de aptitud era negativa
