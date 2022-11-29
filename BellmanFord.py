import numpy as np, csv

result = np.array(list(csv.reader(open("LINFO1114_projet/matrix.csv", "r"), delimiter=";"))).astype("float")
print (result[1][3])

def Bellman_Ford (C : np. matrix ):
    print ("0")