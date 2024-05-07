from sklearn.cluster import KMeans
import numpy as np
from Problem import Problem
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


problem = Problem("./data/2-2024.txt")

Arreglo__Kmeans = []
for i in range(1,problem.m+1):
    Arreglo__Kmeans.append([i, problem.T[i-1].count(1)])#Cambiar la g a NT T[i-1].count(1)

X = np.array(Arreglo__Kmeans) 
n_clusters=4
kmeans = KMeans(n_clusters) 
kmeans.fit(X)
labels = kmeans.labels_ # Como redistribuyo los datos (a q cluster pertenecen)
centroids = kmeans.cluster_centers_

#print("Labels:", labels)
print("Centroids:", centroids)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=100, label='Centroids')
plt.xlabel('Proyecto')
plt.ylabel('Numero de tares por proyecto')
plt.title('Clustering K-means')
plt.legend()
plt.show()

#Nuestra heuristica que escoge el valor de interes
cluster_interes=[]
for i in range(n_clusters):
    cluster_interes.append(centroids[i][1]) # Crear una lista para almacenar el valor mas alto de interes de nuestro eje Y
#print(cluster_interes)
sorted_cluster_interes = sorted(cluster_interes, reverse=True) # Ordenar la lista en orden descendente
top_values = sorted_cluster_interes[:2] # Obtener los dos valores más altos
top_indices = [cluster_interes.index(value) for value in top_values] # Obtener los índices de los dos valores más altos en la lista original
#print("Índices de los dos valores más altos:", top_indices)
indices = []
# Iterar sobre el arreglo con enumerate()
for indice, valor in enumerate(labels):
    # Verificar si el valor es igual a 1 o 0
    if valor == top_indices[0] or valor == top_indices[1]:
        # Si es así, añadir el índice a la lista de índices
        indices.append(indice)
#print(indices)

#print(len(indices))

ganancias=[]
Tareas = []
nuevo_txt=[]

nuevo_txt.append(len(indices))
nuevo_txt.append(problem.n)
nuevo_txt.append(problem.B)



for j in range(len(indices)):
    ganancias.append(problem.g[indices[j]])
nuevo_txt.append(ganancias)
#print("la ganancia es ",len(ganancias))
#print(len(nuevo_txt[3]))
nuevo_txt.append(problem.c)
#print("costos",len(problem.c))
#print(len(nuevo_txt[4]))
for c in range(len(indices)):   
    Tareas.append(problem.T[indices[c]])
nuevo_txt.append(Tareas)

#print("numero de tareas",len(Tareas))
#print(len(nuevo_txt[5]))

#print(nuevo_txt)

def Escribirtxt(numero, archivo):
    with open(archivo, 'w') as f:
        #f.write(str(type(numero)) + '\n')
        f.write(str(numero[0]) + '\n')
        f.write(str(numero[1]) + '\n')
        f.write(str(numero[2]) + '  \n')
        f.write(Escribir_linea(numero[3]) + ' \n')
        f.write(Escribir_linea(numero[4]) + ' \n')
        for i in range(len(numero[5])):
            if i == len(numero[5]):
                f.write(Escribir_linea(numero[5][i]) + ' ')
            else:
                f.write(Escribir_linea(numero[5][i]) + ' \n')

def Escribir_linea(numero):
    # Cocatenar todos los elementos del array en una sola línea
    linea = ' '.join(map(str, numero))
    # Escribir la línea en el archivo
    return(linea)

Escribirtxt(nuevo_txt, "2-2024_mejor_2.txt")