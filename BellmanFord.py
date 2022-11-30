import numpy as np, csv

C = np.array(list(csv.reader(open("LINFO1114_projet/matrix.csv", "r"), delimiter=";"))).astype("float")
print (C[1][3])

def Bellman_Ford (C : np. matrix ):
    # Python3 program for Bellman-Ford's
# single source shortest path algorithm.
from sys import maxsize 

#Exemple TIM

# The main function that finds shortest
# distances from src to all other vertices
# using Bellman-Ford algorithm. The function
# also detects negative weight cycle
# The row graph[i] represents i-th edge with
# three values u, v and w.
def BellmanFord(graph, V, E, src):

	# Initialize distance of all vertices as infinite.
	dis = [maxsize] * V

	# initialize distance of source as 0
	dis[src] = 0

	# Relax all edges |V| - 1 times. A simple
	# shortest path from src to any other
	# vertex can have at-most |V| - 1 edges
	for i in range(V - 1):
		for j in range(E):
			if dis[graph[j][0]] + \
				graph[j][2] < dis[graph[j][1]]:
				dis[graph[j][1]] = dis[graph[j][0]] + \
									graph[j][2]
	print("Vertex Distance from Source")
	for i in range(V):
		print("%d\t\t%d" % (i, dis[i]))

# Driver Code
if __name__ == "__main__":
	V = 5 # Number of vertices in graph
	E = 8 # Number of edges in graph

	# Every edge has three values (u, v, w) where
	# the edge is from vertex u to v. And weight
	# of the edge is w.
	graph = [[0, 1, -1], [0, 2, 4], [1, 2, 3],
			[1, 3, 2], [1, 4, 2], [3, 2, 5],
			[3, 1, 1], [4, 3, -3]]
	BellmanFord(graph, V, E, 0)

# This code is contributed by
# sanjeev2552
