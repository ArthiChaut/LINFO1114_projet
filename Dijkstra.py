import numpy as np
import csv
G = np.array(list(csv.reader(
    open("matrix.csv", "r"), delimiter=";"))).astype("float")
print(G)
Inf = 1.e+12


def dijkstraDist(G, depart):
    # On récupère le nombre de sommets du graphe
    N = np.size(G, 0)

    # Initialisation du tableau des plus courts chemins
    # Le booléen pour savoir si le sommet a déjà été sélectionné
    pcc = list()
    for i in range(N):
        pcc.append([Inf, False])
    sommet_u = depart
    dist_u = 0
    pcc[depart][0] = 0
    # Le premier sommet sélectionné est le sommet depart
    pcc[depart][1] = True

    # On compte le nombre de sommets sélectionnés
    cpt = 0
    while cpt != N-1:
        # À chaque étape, la solution optimale doit être conservée
        # (pour sélection du sommet correspondant à l’étape suivante)
        minimum = Inf
        # Étape de relâchement
        for k in range(N):

            # Si le sommet k n’a pas encore été sélectionné
            if pcc[k][1] == False:
                dist_uv = G[sommet_u][k]
                # Distance totale du chemin s -> ... -> u -> v
                dist_totale = dist_u + dist_uv

                # Mise à jour du tableau des plus courts chemins
                if dist_totale < pcc[k][0]:
                    pcc[k][0] = dist_totale

            # Mise à jour de la solution minimale à cette étape
                if pcc[k][0] < minimum:
                    minimum = pcc[k][0]
                    prochain_sommet_select = k

        # On a traité complétement un sommet
        cpt = cpt + 1

        # Le sommet à traiter est sélectionné et d[u] est mis à jour
        sommet_u = prochain_sommet_select
        pcc[sommet_u][1] = True
        dist_u = pcc[sommet_u][0]

    return (pcc)

#fusion des lignes individuelles en matrice
def dijkstra_matrix(matrix):
    result = []
    for i in range(len(matrix)):
        temp = []
        dijk_line = dijkstraDist(matrix, i)
        for j in range(len(matrix)):
            temp.append(int(dijk_line[j][0]))
        result.append(temp)
    return result


print(np.array(dijkstra_matrix(G)))
