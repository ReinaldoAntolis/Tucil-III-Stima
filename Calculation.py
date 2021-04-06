from math import radians, cos, sin, asin, sqrt
# from Tools import searchPos
# from __main__ import *

# Menghitung jarak antara dua titik di bumi dengan 
# menggunakan garis lintang dan garis bujur
def haversine(pos1, pos2, simpul):
    # Mengubah titik desimal menjadi radian
    lat1, lon1 = simpul[pos1][0], simpul[pos1][1]
    lat2, lon2 = simpul[pos2][0], simpul[pos2][1]
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Rumus perhitungan haversine
    # r merupakan radius bumi dalam satuan kilometer
    r = 6371
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    h = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    x = asin(sqrt(h)) 
    result = 2 * x * r
    return result

def aStar (start, goal, matrix, nodeCount) :
    currNode = start
    dFromStart = 0
    while (currNode != goal) :
        min = None
        minPos = None
        isFirst = True
        for i in range (nodeCount) :
            if (matrix[searchPos(currNode)][i] != 0) :
                if isFirst :
                    isFirst = False
                    minPos = i
                    min = evalFunc(dFromStart, currNode, simpul[i][2], goal)
                else :
                    if (min > evalFunc(dFromStart, currNode, simpul[i][2], goal)) :
                        minPos = i
                        min = evalFunc(dFromStart, currNode, simpul[i][2], goal)

        dFromStart = gn(dFromStart, currNode, simpul[minPos][2]) 
        currNode = simpul[minPos][2]
    return currNode

def evalFunc (dFromStart, currNode, exploreNode, goal) :
    fn = gn (dFromStart, currNode, exploreNode) + hn(exploreNode, goal)
    return fn

def gn (dFromStart, currNode, exploreNode) :
    result = dFromStart + matrix[searchPos(currNode)][searchPos(exploreNode)]
    return result
    
def hn (exploreNode, goal) :
    return haversine (searchPos(exploreNode), searchPos(goal))