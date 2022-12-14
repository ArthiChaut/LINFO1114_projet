import numpy as np

def Floyd_Warshall(C: np.matrix):
    # boucle principale permettant l'itération pour les noeuds intermédiaires
    for k in range(len(C[0])):
        for i in range(len(C[0])):
            # boucle i et j pour chaque paire de coordonnées dans la matrice de distances
            for j in range(len(C[0])):
                if (C[i][j] > C[i][k]+C[k][j]):
                    # si le chemin de i a j et plus court par en passant par le noeud intermédiaire : remplacer la valeur du chemin le plus court
                    C[i][j] = C[i][k]+C[k][j]
    return C
