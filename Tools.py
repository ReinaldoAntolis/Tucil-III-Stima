from Main import *

def searchPos(namaTempat) : 
    found = False
    for i in range (len(simpul)) : 
        if (simpul[i][2] == namaTempat) : 
            return i
    if(not found) : 
        return -1