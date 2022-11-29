import numpy as np, csv

result = np.array(list(csv.reader(open("matrix.csv", "r"), delimiter=";"))).astype("float")
print (result)

def Dijkstra (C : np.matrix ):
    print ("0")