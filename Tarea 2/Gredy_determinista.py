from Problem import DataNode

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
for j in range (len(data_node.clinic_demand_places)):
    data_node.clinic_demand_places[j].sort()
    if data_node.clinic_demand_places[j][0] in Verificador:
        #No hace nada
        int = 1
    else:
        FO = FO + data_node.installation_cost[data_node.clinic_demand_places[j][0]]
        Verificador.append(data_node.clinic_demand_places[j][0])

print("Valor de la Funcion Objetivo:",FO)


