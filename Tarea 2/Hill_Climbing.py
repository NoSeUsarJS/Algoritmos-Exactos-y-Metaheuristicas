import random

def objective_function(x):
    """ Función objetivo de ejemplo. Aquí puedes definir tu propia función a maximizar o minimizar. """
    return -(x ** 2)  # Queremos encontrar el máximo de esta función

def hill_climbing(max_iter=1000, step_size=0.1):
    """ Algoritmo de Hill Climbing para maximizar una función. """
    # Comenzamos desde un punto aleatorio
    current_solution = random.uniform(-10, 10)
    print("Punto de inicio:", current_solution)
    
    for i in range(max_iter):
        # Evaluamos el valor actual
        current_value = objective_function(current_solution)
        
        # Generamos un nuevo punto vecino
        new_solution = current_solution + random.uniform(-step_size, step_size)
        new_value = objective_function(new_solution)
        
        # Si el nuevo valor es mejor, actualizamos la solución actual
        if new_value > current_value:
            current_solution = new_solution
            current_value = new_value
    
    # Después de iterar, devolvemos la mejor solución encontrada
    return current_solution, objective_function(current_solution)

# Ejemplo de uso del algoritmo Hill Climbing
best_solution, best_value = hill_climbing()
print("Mejor solución encontrada:", best_solution)
print("Valor máximo encontrado:", best_value)
