import numpy as np

def bellman_ford_lane(matrix, source):
  # Initialisation de la distance du sommet source à 0 et des autres à infini
  # Et le prédécesseur de chaque sommet à None
  distances = [float("inf")] * len(matrix)
  predecessors = [None] * len(matrix)
  distances[source] = 0

  #On répète le processus pour chaque sommet
  #Calculer la distance la plus courte entre le sommet source et chaque sommet
  for i in range(len(matrix) - 1):
    for u in range(len(matrix)):
      for v in range(len(matrix)):
        if matrix[u][v] is not None and distances[u] + matrix[u][v] < distances[v]:
          distances[v] = distances[u] + matrix[u][v]
          predecessors[v] = u

  return distances

#Boucle pour chaque ligne (sommet différent) de la matrice
def Bellman_Ford(C : np.matrix):
	finalMatrix = list()
	for i in range(len(C)):
		finalMatrix.append(bellman_ford_lane(C,i))
	return np.array(finalMatrix)

