#importation des fonctions et modules nécessaires
from Bellman_Ford import Bellman_Ford
from Floyd_Warshall import Floyd_Warshall
from Dijkstra import Dijkstra
import numpy as np,csv

#Ouverture du fichier csv en mode lecture et faisant une conversion en matrice
C = np.array(list(csv.reader(open("matrix.csv", "r"), delimiter=","))).astype("float")

#Lancement des algorithmes
if __name__ == "__main__":
    print(C)
    print(Bellman_Ford(C))
    print(Dijkstra(C))
    print(Floyd_Warshall(C))