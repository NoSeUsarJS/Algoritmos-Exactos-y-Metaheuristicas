import random
from Problem import DataNode 

data_node = DataNode.ReadData("data/C1.txt")


Verificador = []

FO = 0

def dividir_lista(lista):
    if len(lista) != 1:
        punto_medio = len(lista) // 2
        primera_mitad = lista[:punto_medio]
        segunda_mitad = lista[punto_medio:]
        Aleatorio = random.random()
        if Aleatorio <= 0.9:
            return dividir_lista(primera_mitad)
        else:
            return dividir_lista(segunda_mitad)
    else:
        return lista[0]
        

FO = 0
for j in range (len(data_node.clinic_demand_places)):
    Valor = dividir_lista(data_node.clinic_demand_places[j])

    if Valor in Verificador:
        #No hace nada
        int = 1
    else:
        FO = FO + data_node.installation_cost[Valor]
        Verificador.append(Valor)

print("Valor de la Funcion Objetivo:",FO)

Solucion = []

for j in range (len(data_node.installation_cost)):
    if j in Verificador:
        Solucion.append(1)
    else:
        Solucion.append(0)


