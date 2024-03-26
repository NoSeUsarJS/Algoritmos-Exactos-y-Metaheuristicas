from sklearn.cluster import KMeans
import numpy as np

# Genera algunos datos de ejemplo
X = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]]) #Agregar aqui los datos generados por el MFC?

# Especifica el número de clústeres
kmeans = KMeans(n_clusters=4) # importante en base al modelo 

# Entrena el modelo K-means
kmeans.fit(X)

# Obtiene las etiquetas de los clústeres
labels = kmeans.labels_

# Obtiene los centroides de los clústeres
centroids = kmeans.cluster_centers_

print("Labels:", labels)
print("Centroids:", centroids)
