import numpy as np
import csv

result = np.array(
    list(csv.reader(open("LINFO1114_projet\matrix.csv", "r"), delimiter=";"))).astype("float")
print(result)


def Floyd_Warshall(C: np.matrix):
    for k in range(len(C[0])):
        for i in range(len(C[0])):
            for j in range(len(C[0])):
                if (C[i][j] > C[i][k]+C[k][j]):
                    C[i][j] = C[i][k]+C[k][j]
    return C


test = [[0, 5, 3, 3], [5, 0, 5, 100], [3, 5, 0, 4], [3, 100, 4, 0]]
test_graph_7 = [[0, 5, 3, 3, 999, 999, 999, 999, 999, 999], [5, 0, 5, 999, 3, 999, 4, 999, 999, 999], [3, 5, 0, 4, 1, 5, 999, 999, 999, 999], [3, 999, 4, 0, 999, 1, 999, 999, 5, 999], [999, 3, 1, 999, 0, 3, 2, 3, 999, 999], [
    999, 999, 5, 1, 3, 0, 999, 2, 3, 999], [999, 4, 999, 999, 2, 999, 0, 2, 999, 4], [999, 999, 999, 999, 3, 2, 2, 0, 4, 5], [999, 999, 999, 5, 999, 3, 999, 4, 0, 4], [999, 999, 999, 999, 999, 999, 4, 5, 4, 0]]
print(Floyd_Warshall(result))
