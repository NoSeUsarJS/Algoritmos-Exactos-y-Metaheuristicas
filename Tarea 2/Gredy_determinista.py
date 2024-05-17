from Problem import DataNode
import time

data_node = DataNode.ReadData("data/C1.txt")

#print(data_node.installation_cost)
#print(data_node.clinic_demand_places[0])
#sum = 0
#for i in range (len(data_node.clinic_demand_places[0])):
#    print(data_node.clinic_demand_places[0][i])
#    print(data_node.installation_cost[data_node.clinic_demand_places[0][i]])
#    sum = sum + data_node.installation_cost[data_node.clinic_demand_places[0][i]]
#    print(f"Suma actual:",sum)

Verificador = []


FO = 0
start_time = time.time()
for j in range (len(data_node.clinic_demand_places)):
    data_node.clinic_demand_places[j].sort()
    if data_node.clinic_demand_places[j][0] in Verificador:
        #No hace nada
        int = 1
    else:
        FO = FO + data_node.installation_cost[data_node.clinic_demand_places[j][0]]
        Verificador.append(data_node.clinic_demand_places[j][0])
end_time = time.time()
execution_time = end_time - start_time
print("Valor de la Funcion Objetivo:",FO, "Se ejecuto en:",execution_time)
#print("Posiciones donde se instalaron las clinicas: ", Verificador)
Solucion = []
for j in range (len(data_node.installation_cost)):
    if j in Verificador:
        Solucion.append(1)
    else:
        Solucion.append(0)
        
#print("Conjunto Solucion:",Solucion )

