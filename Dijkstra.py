import numpy as np
Inf = 1.e+12

#fonction qui permet de calculer toutes les distances à partir d'un noeud de départ
def dijkstra(C, start):
    #On récupère le nombres de noeuds
    nbr_node = len(C[0])
    result = []
    #On crée une liste qui va contenir les distances les plus courtes du graphe
    #Les bouléens vont permettre de savoir si on a déjà trouvé le chemin le plus court
    for i in range(nbr_node):
        result.append([Inf, False])
    node = start
    distance_start = 0
    #On ajoute à la liste le noeuds de départ et on le met à True pour dire qu'il est sélèctionné
    result[start][0] = 0
    result[start][1] = True
    
    for j in range(nbr_node):
        minimum = Inf
        #cette boucle va nous permettre de comparer tout les noeuds pour déterminer le chemin le plus court d'un noeud à un autre
        for k in range(nbr_node):
            #on verifie si on a déjà trouver le chemin le plus court de ce noeuds
            #Si on a pas encore trouvé on calcule les distances et on les compares pour trouver le plus court chemins 
            if result[k][1] == False:
                distance = C[node][k]
                distance_total = distance_start + distance
                if distance_total < result[k][0]:
                    result[k][0] = distance_total
                if result[k][0] < minimum:
                    minimum = result[k][0]
                    node_next = k
        
        node = node_next
        #On enregistre le plus court en le mettant en True
        result[node][1] = True
        distance_start = result[node][0]

    return(result)

#fusion des lignes individuelles en matrice 
def dijkstra_matrix(matrix):
    result = []
    for i in range(len(matrix)):
        temp = []
        dijk_line = dijkstra(matrix, i)
        for j in range(len(matrix)):
            temp.append(int(dijk_line[j][0]))
        result.append(temp)
    return np.array(result)
