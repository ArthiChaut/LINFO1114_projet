import numpy as np, csv

result = np.array(list(csv.reader(open("matrix.csv", "r"), delimiter=";"))).astype("float")
print (result)

def Floyd_Warshall (C : np.matrix ):
    print ("0")

Floyd_Warshall()