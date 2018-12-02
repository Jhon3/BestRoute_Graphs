import numpy as np
import time
import sys
import networkx as nx
sys.path.insert(0, '../') 
from dijkstra import Dijkstra

class TestAlgorithm:

    def __init__(self, amountOfTest):
        self.amountOfTest = amountOfTest
        self.resultProcess = np.zeros([amountOfTest, 9]) #Matriz que armazena: Origem | Destino | Custo_direto(se houver )| Menor_custo (aplicando algoritmo criado de menor caminho) | Tempo Médio | Desvio Padrão | Menor_custo(networkx) | Tempo Médio (networkx) | Desvio Padrão
    
    def getResultProcess(self):
        multiplicator = 2
        startOfVertices = 4 

        for x in range(0, self.amountOfTest):
            
            matrix = np.loadtxt('./dataSets/dataSet-'+str(startOfVertices)+'.txt', dtype=int) #Load a matrix using in other file
            #A origem será sempre a partir do primeiro vertice (0)
            self.setDestination(matrix, x)
            self.setOrginalCost(matrix, x)
            self.setBestCost(matrix, x)
            self.saveExperimentResult()
            self.networkxEvaluation(matrix, x) #Apresenta erro para um caso onde há uma quantidade grande de vertices
            self.saveExperimentResult()
            print("Caso: " + str(startOfVertices))
            startOfVertices*=multiplicator
        return self.resultProcess
    
    def saveExperimentResult(self):
        np.savetxt('./resultProcess.txt', self.resultProcess, fmt='%f')

    def setDestination(self, dataSet, index):   #1 - Preenchendo a segunda coluna da matrix
        destination = np.size(dataSet, 1)-1
        self.resultProcess[index,1 ] = destination
        
    def setOrginalCost(self, dataSet, index):
        destination = np.size(dataSet, 1)-1
        if dataSet[0, destination] != 0:
            self.resultProcess[index, 2] = dataSet[0, destination]
        else:
            self.resultProcess[index, 2] = 999

    
    def setAvgAndStd(self, listOfValues, index, indexAVG, indexSTD):
        self.resultProcess[index, indexAVG] = np.mean(listOfValues)
        self.resultProcess[index, indexSTD] = np.std(listOfValues)

    def setBestCost(self, dataSet, index):
        bestCost = 0
        n = np.size(dataSet, 1)
        source = 0
        destination = n-1
        timeList = []
        dijkstra = Dijkstra(source, destination, dataSet, n)
        for x in range(0, 30):
            firstTime = time.time()
            bestroute = dijkstra.dijkstraRoute()
            lastTime = time.time()
            timeList.append(lastTime - firstTime)
            bestCost = bestroute[1]
        self.resultProcess[index, 3] = bestCost
        self.setAvgAndStd(timeList, index, 4, 5)
    
    def networkxEvaluation(self, dataSet, index):
        bestCost = 0
        n = np.size(dataSet, 1)
        source = 0
        destination = n -1
        timeList = []

        g = nx.MultiDiGraph()
        
        for x in range(0, n):
            for y in range(0, n):
                if dataSet[y,x] != 0:
                    g.add_edge(x, y, weight=dataSet[y,x])
        
        for x in range(0, 30):
            firstTime = time.time()
            bestCost = nx.dijkstra_path_length(g, destination, source)
            lastTime = time.time()
            timeList.append(lastTime - firstTime)
        self.resultProcess[index, 6] = bestCost
        self.setAvgAndStd(timeList, index, 7, 8)


    def comparingRoute(self, matrix):
        #matrix = np.loadtxt('./dataSets/dataSet-40.txt', dtype=int)
        n = np.size(matrix, 1)
        source = 0
        destination = n -1

        g = nx.MultiDiGraph()
        for x in range(0, n):
            for y in range(0, n):
                g.add_edge(x, y, weight=matrix[y,x])
        dijkstra = Dijkstra(source, destination, matrix, n)

        print("my algorith: "+ str(dijkstra.dijkstraRoute()[0]))
        print("network: "+ str(nx.dijkstra_path(g, source, destination)))

if __name__ == '__main__':
    resultProcess = TestAlgorithm(11)
    resultProcess.getResultProcess()
