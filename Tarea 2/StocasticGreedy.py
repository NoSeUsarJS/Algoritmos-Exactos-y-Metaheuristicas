from DataNode import DataNode
import time
import random

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

start_time = time.time()

for i in range (len(data_node.clinic_demand_places)):
    if not have_common_places(checker, data_node.clinic_demand_places[i]):

        data_node.clinic_demand_places[i].sort()

        selected_place = random_selection(data_node.clinic_demand_places[i])

        fo = fo + data_node.installation_cost[selected_place-1]
        checker.append(selected_place)
        
end_time = time.time()
execution_time = end_time - start_time

print(f"FO value: {fo}")
print(f"Execution time: {execution_time}")

solution = []
for j in range (len(data_node.installation_cost)):
    if j in checker:
        solution.append(1)
    else:
        solution.append(0)

#print(f"FO value second check: {data_node.get_FO_value(solution)}")
        
#print("Solution:",solution )

