'''
1. Build an initial solution using the stocastic greedy algorithm.
2. Compare the solution with the neighborhood using the Objective Function.
3. Go for the best quality solution.
'''

from DataNode import DataNode
from BuildSolution import build_solution
from time import time

def hill_climbing(current_solution: list, data_node: DataNode):
    neighborhood = []
    #VERIFICAR QUE TODOS LOS SECTORES ESTÉN CUBIERTOS FALTA ESO
    for i in range(len(current_solution)):
        new_solution = current_solution.copy()
        if new_solution[i] == 1:
            new_solution[i] = 0
        else:
            new_solution[i] = 1

        neighborhood.append(new_solution)
    
    best_solution = current_solution    
    min_OF_value = data_node.get_OF_value(best_solution)

    for solution in neighborhood:
        current_OF_value = data_node.get_OF_value(solution)

        if current_OF_value < min_OF_value:
            best_solution = solution
            min_OF_value = current_OF_value
    
    return best_solution

data_node = DataNode("data/C1.txt")

initial_solution = build_solution(data_node)

print(data_node.get_OF_value(initial_solution))

start_time = time()

best_solution = initial_solution

while time() - start_time < 30:
    best_solution = hill_climbing(best_solution, data_node)
    print(data_node.get_OF_value(best_solution))

print(data_node.get_OF_value(best_solution))