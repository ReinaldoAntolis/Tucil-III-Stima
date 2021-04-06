# import Calculation
from __main__ import *

def input(nama_file) : 
    simpul = []
    matrix = []
    with open(nama_file) as f:
        lines = f.readlines()

    lineNumber = 0
    nodeCount = 0
    for line in lines:
        if (lineNumber == 0) : 
            nodeCount = int(line)
        else : 
            if (lineNumber < nodeCount + 1) :
                temp = line.split()
                temp[0] = float(temp[0])
                temp[1] = float(temp[1])
                simpul.append(temp)
            else : 
                temp = line.split()
                for i in range (len(temp)) : 
                    temp[i] = int(temp[i])
                matrix.append(temp)
        lineNumber += 1
    return simpul,matrix,nodeCount 

def searchPos(namaTempat) : 
    found = False
    for i in range (len(simpul)) : 
        if (simpul[i][2] == namaTempat) : 
            return i
    if(not found) : 
        return -1


#change adjacency matrix from boolean to weighted
def changeMatrix() : 
    for i in range(nodeCount) : 
        for j in range(i, nodeCount) : 
            if(matrix[i][j] != 0) : 
                temp = haversine(simpul[i][0], simpul[i][1], simpul[j][0], simpul[j][1])
                matrix[i][j] = temp
                matrix[j][i] = temp

simpul, matrix, nodeCount = input("ITB.txt")
# changeMatrix()
# for test in matrix :
#     print(test)

print (aStar("Simpang_McD", "Tubagus_Ismail", matrix, nodeCount))




