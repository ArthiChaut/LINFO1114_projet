#importation des fonctions et modules nécessaires
from Bellman_Ford import Bellman_Ford
from Floyd_Warshall import Floyd_Warshall
from Dijkstra import Dijkstra
import numpy as np,csv

#Ouverture du fichier csv en mode lecture et faisant une conversion en matrice
C = np.array(list(csv.reader(open("matrix.csv", "r"), delimiter=","))).astype("float")

#Lancement des algorithmes
if __name__ == "__main__":
    print("-------------------Matrice initiale------------------", C, sep="\n")
    print("--------Matrice après Bellman-Ford--------", Bellman_Ford(C), sep="\n")
    print("--------Matrice Dijkstra--------", Dijkstra(C), sep="\n")
    print("----------Matrice Floyd-Warshall----------", Floyd_Warshall(C), sep="\n")