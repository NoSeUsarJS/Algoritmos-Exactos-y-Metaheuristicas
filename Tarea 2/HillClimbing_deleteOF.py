'''
1. Build an initial solution using the stocastic greedy algorithm.
2. Compare the solution with the neighborhood using the Objective Function.
3. Go for the best quality solution.
'''

from DataNode import DataNode
from BuildSolution import build_solution
from time import time
import matplotlib.pyplot as plt
import random 

def Check_restriction(vecino: list, subconjuntos: list):
    for i in range (len(subconjuntos)):
        sum = 0
        for j in range (len(subconjuntos[i])):

            if vecino[subconjuntos[i][j]-1] == 1:
                sum = sum + 1
            #print("Sector:",i, "numero",j,"Valor: ",solution[data_node.clinic_demand_places[i][j]-1], "suma: ",sum)
        if sum < 1: 
            return False
    return True

def hill_climbing(current_solution: list, data_node: DataNode):
    neighborhood = []
    probar = False
    while(probar != True):
        for i in range(len(current_solution)):
            prob = random.random()
            if prob < 0.5 and current_solution[i] == None:
                current_solution[i] = 1
            elif current_solution[i] == None and prob >= 0.5:
                current_solution[i] = 0
        probar = Check_restriction(current_solution,data_node.clinic_demand_places)

    #for i in range
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
        if Check_restriction(solution,data_node.clinic_demand_places) == True:
            current_OF_value = data_node.get_OF_value(solution)
            
            if current_OF_value < min_OF_value:
                best_solution = solution
                min_OF_value = current_OF_value
    
    return best_solution
data_node = DataNode("data/C1.txt")

def have_common_places(list1, list2):
    return len(set(list1).intersection(set(list2))) > 0

def random_selection(list: list) -> int:
    N = len(list)
    weights = [N**4-i**4 for i in range(N)]
    
    total_weight = sum(weights)
    rand_num = random.uniform(0, total_weight*0.1)
    cumulative_weight = 0
    for i, weight in enumerate(weights):
        cumulative_weight += weight
        if rand_num <= cumulative_weight:
            return list[i]


checker = []

fo = 0


for i in range (len(data_node.clinic_demand_places)):
    if not have_common_places(checker, data_node.clinic_demand_places[i]):

        data_node.clinic_demand_places[i].sort()

        selected_place = random_selection(data_node.clinic_demand_places[i])

        fo = fo + data_node.installation_cost[selected_place-1]
        checker.append(selected_place)


initial_solution = []
for j in range (len(data_node.installation_cost)):
    if j+1 in checker:
        initial_solution.append(1)
    else:
        initial_solution.append(0)

initial_solution = build_solution(data_node)

n = 0
while(n != data_node.n):
    prob = random.random()
    if prob < 0.5:
        initial_solution[n] = None
    n = n + 1
#print(initial_solution)
best_solution = initial_solution

x = []
y = []
start_time = time()
while time() - start_time < 60:
#n = 50
#while(n != 0):
    best_solution = hill_climbing(best_solution, data_node)
    print(data_node.get_OF_value(best_solution))
    x.append( time()-start_time)
    #x.append(n)
    y.append(data_node.get_OF_value(best_solution))
    n=n-1

#x.sort()
print("Valor de la funcion objetivo",data_node.get_OF_value(best_solution), "Tiempo de procesamiento",time()-start_time)
#print(x,y)

plt.plot(x, y)
plt.title('Gráfico de funcion objetivo vs tiempo')
#plt.xlabel('Iteracion')
plt.xlabel('Tiempo (seg)')
plt.ylabel('Valor de funcion objetivo ($)')

# Mostrar el gráfico
plt.show()