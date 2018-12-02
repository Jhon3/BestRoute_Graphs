import numpy as np
from random import randint

class GenereteDataSet:

    def __init__(self):
        pass
        
    def generete(self, sizeOfDataSet):
        n = sizeOfDataSet
        matrixTest = [[randint(0, 20) for x in range(n)] for y in range(n)]

        for x in range(n):
            for y in range(n):
               if x == y: matrixTest[x][y]= 0
        return matrixTest


    def manyDataSet(self, amount):
        sizeStart = 4 #caso de teste inicia com 4 vertices.
        multiplicator = 2 #a cada iteração a quantidade de vertices é multiplicada por 2.
        for x in range(0, amount):
            matrix = self.generete(sizeStart)
            np.savetxt('./dataSets/dataSet-'+ str(sizeStart) + '.txt', matrix, fmt='%d')
            sizeStart *= multiplicator
            #matrix2 = np.loadtxt('outfile.txt', dtype=int) #Load a matrix using in other file

if __name__ == '__main__':
    genereteData = GenereteDataSet()
    genereteData.manyDataSet(11) #indica quantos casos de texte deseja
    
