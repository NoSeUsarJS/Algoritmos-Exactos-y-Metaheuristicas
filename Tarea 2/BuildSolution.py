import random
from DataNode import DataNode

def have_common_places(list1, list2):
    return len(set(list1).intersection(set(list2))) > 0

def random_selection(list: list) -> int:
    N = len(list)
    weights = [N**4-i**4 for i in range(N)]
    
    total_weight = sum(weights)
    rand_num = random.uniform(0, total_weight)
    cumulative_weight = 0
    for i, weight in enumerate(weights):
        cumulative_weight += weight
        if rand_num <= cumulative_weight:
            return list[i]

def build_solution(data_node: DataNode) -> list:
    checker = []

    for i in range (len(data_node.clinic_demand_places)):
        if not have_common_places(checker, data_node.clinic_demand_places[i]):

            data_node.clinic_demand_places[i].sort()

            selected_place = random_selection(data_node.clinic_demand_places[i])

            checker.append(selected_place)
    
    solution = []
    for j in range (len(data_node.installation_cost)):
        if j+1 in checker:
            solution.append(1)
        else:
            solution.append(0)
    
    return solution