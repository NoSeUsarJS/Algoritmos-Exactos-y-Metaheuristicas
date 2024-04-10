from sklearn.cluster import KMeans
import numpy as np
from MFC import MFC
from Problem import Problem
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


problem = Problem("./data/1-2024.txt")

Arreglo__Kmeans = []
for i in range(1,problem.m+1):
    Arreglo__Kmeans.append([i, problem.g[i-1]])#Cambiar la g a NT o a T para ver otros casos, Para T habria q crear otra funcion

X = np.array(Arreglo__Kmeans) 
kmeans = KMeans(n_clusters=4) 
kmeans.fit(X)
labels = kmeans.labels_ # Como redistribuyo los datos (a q cluster pertenecen)
centroids = kmeans.cluster_centers_

print("Labels:", labels)
print("Centroids:", centroids)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=100, label='Centroids')
plt.xlabel('Proyecto')
plt.ylabel('Ganancia del proyecto')
plt.title('Clustering K-means')
plt.legend()
plt.show()