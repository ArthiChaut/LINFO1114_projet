import numpy, csv

result = numpy.array(list(csv.reader(open("matrix.csv", "rb"), delimiter=";"))).astype("float")
print (result)

def Dijkstra (C : np.matrix ):
    print ("0")