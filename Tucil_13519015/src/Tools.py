from math import radians, cos, sin, asin, sqrt
import os

def readFile(nama_file) : 
    simpul = [] # Menyimpan list tuple dengan tuple (latitude, longitude, nama simpul)
    matrix = [] # Menyimpan adjacency matrix
    # Membaca file
    filepath = os.path.join('..\\test', nama_file)
    with open(filepath) as f:
        lines = f.readlines()

    lineNumber = 0
    nodeCount = 0
    for line in lines:
        # lineNumber == 0 membaca jumlah node
        if (lineNumber == 0) : 
            nodeCount = int(line)
        else : 
            # Kasus membaca simpul
            if (lineNumber < nodeCount + 1) :
                temp = line.split()
                temp[0] = float(temp[0])
                temp[1] = float(temp[1])
                simpul.append(temp)
            # Kasus membaca adjacency matrix
            else : 
                temp = line.split()
                for i in range (len(temp)) : 
                    temp[i] = int(temp[i])
                matrix.append(temp)
        lineNumber += 1
    return simpul,matrix,nodeCount 

# Mencari indeks dari suatu nama tempat di array simpul
def searchPos(namaTempat) : 
    found = False
    for i in range (len(simpul)) : 
        if (simpul[i][2] == namaTempat) : 
            return i
    if(not found) : 
        return -1

# Mengubah adjacency matrix dari berisi boolean menjadi berisi weighted
def changeMatrix() : 
    for i in range(nodeCount) : 
        for j in range(i, nodeCount) : 
            if(matrix[i][j] != 0) : 
                temp = haversine(searchPos(simpul[i][2]), searchPos(simpul[j][2]))
                matrix[i][j] = temp
                matrix[j][i] = temp

# Menghitung jarak antara dua titik di bumi dengan 
# menggunakan garis lintang dan garis bujur
def haversine(pos1, pos2):
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

def aStar(start, goal) : 
    # Inisiasi
    stack = []  # Stack yang menyimpan jalur yang dilalui (jalur terpendek disimpan disini)
    visitedNodes = [] # Array boolean, menyimpan nodes yang sudah dilewati
    currNode = start    # Node saat ini
    stack.append(start) 
    dFromStart = 0 # Jarak dari simpul asal
    found = False # Boolean yang mengecek apakah sudah mencapai simpul tujuan

    # Loop selama stack tidak kosong dan simpul tujuan belum ditemukan
    while(len(stack) > 0 and found == False) : 
        # Inisialisasi nilai
        # nilai fungsi evaluasi paling minimal
        min = None
        minPos = None
        # boolean untuk mengecek apakah merupakann tetangga pertama yang ditemukan
        isFirst = True
        i = 0
        # boolean untuk mengecek apakah suatu node masih memiliki tetangga
        # yang belum dikunjungi 
        neighbour = False 
        
        # Loop selama jumlah iterasi tidak melebihi jumlah node
        while(i < nodeCount) :
            # Kasus ditemukan sisi yang nilainya tidak nol dan belum  pernah dikunjungi
            if ((matrix[searchPos(currNode)][i] != 0) and (simpul[i][2] not in visitedNodes)) :
                # Kasus sisi yang memenuhi syarat sebelumnya ditemukan pertama kalinya
                if (isFirst) :
                    isFirst = False
                    minPos = i
                    min = evalFunc(dFromStart, currNode, simpul[i][2], goal)
                # Kasus sisi ditemukannya sisi setelah sisi pertama
                else :
                    # Kasus ditemukannya fungsi evaluasi yang lebih minimal
                    if (min > evalFunc(dFromStart, currNode, simpul[i][2], goal)) :
                        minPos = i
                        min = evalFunc(dFromStart, currNode, simpul[i][2], goal)
                # Menandakan mempunyai tetangga yang belum pernah dikunjungi       
                neighbour = True
            i+=1
        # Kasus sudah tidak mempunyai tetangga yang belum pernah dikunjungi
        if (neighbour == False) :
            # Memasukkan currNode ke boolean visitedNodes (menandakan sudah dikunjungi)
            if (currNode not in visitedNodes) :
                visitedNodes.append(currNode)
            # Melakukan backtrack
            temp = stack.pop()
            if (len(stack) > 0) :
                # Mengurangi jarak dari simpul asal yang dicatat (karena backtrack, jadi mundur ke simpul sebelumnya)
                dFromStart -= haversine(searchPos(temp), searchPos(stack[len(stack) - 1]))
                # Backtrack untuk currNode
                currNode = stack[len(stack) - 1]
        else : 
            # Push simpul dengan evaluation function paling minimal
            stack.append(simpul[minPos][2])
            # Memasukkan currNode ke boolean visitedNodes (menandakan sudah dikunjungi)
            if (currNode not in visitedNodes) :
                visitedNodes.append(currNode)
            # Menambah jarak dari simpul asal
            dFromStart = gn(dFromStart, currNode, simpul[minPos][2]) 
            # Mengubah currNode ke simpul dengan evaluation function paling minimal
            currNode = simpul[minPos][2]
        # Kasus simpul tujuan ditemukan
        if (currNode == goal) : 
            found = True
    # Kasus stack kosong, artinya tidak ditemukan jalur
    # antara simpul asal dan simpul tujuan
    if (len(stack) == 0) : 
        # Set jarak dari simpul asal ke simpul tujuan menjadi 0
        dFromStart = 0
    return dFromStart, stack

# Menghitung fungsi evaluasi dengan rumus f(n) = g(n) + h(n)
def evalFunc (dFromStart, currNode, exploreNode, goal) :
    fn = gn (dFromStart, currNode, exploreNode) + hn(exploreNode, goal)
    return fn

# g(n) merupakan fungsi yang menghitung total 
# jarak dari simpul awal menuju exploreNode
def gn (dFromStart, currNode, exploreNode) :
    result = dFromStart + matrix[searchPos(currNode)][searchPos(exploreNode)]
    return result

# h(n) merupakan fungsi yang menghitung jarak 
# garis lurus dari exploreNode menuju simpul tujuan    
def hn (exploreNode, goal) :
    return haversine (searchPos(exploreNode), searchPos(goal))


# Main Program
# Input file kasus uji
kasusUji = input("Masukkan nama file kasus uji: ")
# Mengolah input kasus uji
simpul, matrix, nodeCount = readFile(kasusUji)
# Mencetak semua simpul yang ada
print("List simpul: ")
no = 1
for node in simpul :
    print(no, end="")
    print(".", end="")
    print(node[2])
    no += 1
# Mengubah adjacency matrix yang berisi boolean menjadi
# berisi bobot sisi antar simpul    
changeMatrix()
#Menerima input simpul asal dan simpul tujuan
startNode = int(input("No simpul asal: "))
goalNode = int(input("No simpul tujuan: "))

# Menjalankan algoritma A*
distance, shortestPath = aStar(simpul[startNode - 1][2], simpul[goalNode - 1][2])
# Kasus terdapat lintasan terpendek antara simpul asal dan tujuan
if (len(shortestPath) != 0) :
    print("Jarak lintasan terpendek antara " + simpul[startNode - 1][2] + " dan " + simpul[goalNode - 1][2]
            + " adalah " + str(distance) + " km")
# Kasus tidak terdapat lintasan antara simpul asal dan tujuan
else :
    print("Tidak terdapat lintasan antara " + simpul[startNode - 1][2] + " dan " + simpul[goalNode - 1][2])






