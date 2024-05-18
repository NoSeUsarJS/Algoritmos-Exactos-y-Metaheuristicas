from DataNode import DataNode
import random
import time

data_node = DataNode("data/C1.txt")

def have_common_places(list1, list2):
    return len(set(list1).intersection(set(list2))) > 0

Verificador = []

FO = 0

def dividir_lista(lista):
    if len(lista) != 1:
        punto_medio = len(lista) // 2
        primera_mitad = lista[:punto_medio]
        segunda_mitad = lista[punto_medio:]
        Aleatorio = random.random()
        #print(Aleatorio, primera_mitad, segunda_mitad)
        if Aleatorio <= 0.9: #Determina que tan % es que este en la primera mitad (Nos interesa que este en la primera mitad)
            return dividir_lista(primera_mitad)
        else:
            return dividir_lista(segunda_mitad)
    else:
        return lista[0]
        

FO = 0
start_time = time.time()
for j in range (len(data_node.clinic_demand_places)):
    if not have_common_places(Verificador, data_node.clinic_demand_places[j]):
        Valor = dividir_lista(data_node.clinic_demand_places[j])

        FO = FO + data_node.installation_cost[Valor]
        Verificador.append(Valor)
end_time = time.time()
execution_time = end_time - start_time
print("Valor de la Funcion Objetivo:",FO, "Se ejecuto en:",execution_time)

Solucion = []

for j in range (len(data_node.installation_cost)):
    if j in Verificador:
        Solucion.append(1)
    else:
        Solucion.append(0)

#print("Conjunto Solucion:",Solucion )