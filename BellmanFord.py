import numpy as np, csv
from sys import maxsize 

def bellman_ford(matrix, source):
  # initialize the distances from the source vertex to all other vertices
  # as infinite and the predecessor of each vertex as None
  distances = [float("inf")] * len(matrix)
  predecessors = [None] * len(matrix)
  distances[source] = 0

  # relax the edges repeatedly
  for i in range(len(matrix) - 1):
    for u in range(len(matrix)):
      for v in range(len(matrix)):
        if matrix[u][v] is not None and distances[u] + matrix[u][v] < distances[v]:
          distances[v] = distances[u] + matrix[u][v]
          predecessors[v] = u

  # check for negative-weight cycles
  for u in range(len(matrix)):
    for v in range(len(matrix)):
      if matrix[u][v] is not None and distances[u] + matrix[u][v] < distances[v]:
        raise ValueError("Negative-weight cycle detected.")

  return distances

def BellmanFordFinal(C : np.matrix):
	finalMatrix = list()
	for i in range(len(C)):
		finalMatrix.append(bellman_ford(C,i))
	return finalMatrix



# Driver Code
if __name__ == "__main__":
	C = np.array(list(csv.reader(open("matrix.csv", "r"), delimiter=";"))).astype("float")
	
	V = 5 # Number of vertices in graph
	E = 8 # Number of edges in graph

	# Every edge has three values (u, v, w) where
	# the edge is from vertex u to v. And weight
	# of the edge is w.
	#graph = [[0, 1, -1], [0, 2, 4], [1, 2, 3],
	#		[1, 3, 2], [1, 4, 2], [3, 2, 5],
	#		[3, 1, 1], [4, 3, -3]]
	#BellmanFord(graph, V, E, 0)
	print(BellmanFordFinal(C))

