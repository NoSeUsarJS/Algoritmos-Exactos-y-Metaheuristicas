from Problem import DataNode
import random

data_node = DataNode.ReadData("data/C1.txt")


def numero_mas_cercano(lista, numero):
    return min(lista, key=lambda x: abs(x - numero))

Verificador = []

FO = 0
for j in range (len(data_node.clinic_demand_places)):
    Maxsize = data_node.clinic_demand_places[j][len(data_node.clinic_demand_places[j])-1]
    Probabilidad_indice=random.randint(1,Maxsize)
    #print("Lista", data_node.clinic_demand_places[j])
    #print("numero", Probabilidad_indice)
    Indice_Escojido=numero_mas_cercano(data_node.clinic_demand_places[j],Probabilidad_indice)
    #print("numero2",Indice_Escojido)

    if Indice_Escojido in Verificador:
        #No hace nada
        int = 1
    else:
        FO = FO + data_node.installation_cost[Indice_Escojido]
        Verificador.append(Indice_Escojido)

print("Valor de la Funcion Objetivo",FO)



