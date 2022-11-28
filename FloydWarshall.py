import numpy, csv

result = numpy.array(list(csv.reader(open("matrix.csv", "rb"), delimiter=";"))).astype("float")
print (result)

def Floyd_Warshall (C : np.matrix ):
    print ("0")

Floyd_Warshall()