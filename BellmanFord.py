import numpy, csv

result = numpy.array(list(csv.reader(open("matrix.csv", "rb"), delimiter=";"))).astype("float")
print (result)

def Bellman_Ford (C : numpy. matrix ):
    print ("0")