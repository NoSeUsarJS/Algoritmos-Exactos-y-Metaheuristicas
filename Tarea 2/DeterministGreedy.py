from DataNode import DataNode
import time

data_node = DataNode("data/C1.txt")

def have_common_places(list1, list2):
    return len(set(list1).intersection(set(list2))) > 0

checker = []

fo = 0

start_time = time.time()

for i in range (len(data_node.clinic_demand_places)):
    if not have_common_places(checker, data_node.clinic_demand_places[i]):
        data_node.clinic_demand_places[i].sort()
        
        fo = fo + data_node.installation_cost[data_node.clinic_demand_places[i][0]-1]
        checker.append(data_node.clinic_demand_places[i][0])
        
end_time = time.time()
execution_time = end_time - start_time

print(f"FO value: {fo}")
print(f"Execution time: {execution_time}")

solution = []
for i in range (len(data_node.installation_cost)):
    if i+1 in checker:
        solution.append(1)
    else:
        solution.append(0)

#print(f"FO value second check: {data_node.get_FO_value(solution)}")
        
#print("Solution:",solution )

