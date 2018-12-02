from dataSet import DataSet
import numpy as np

class Dijkstra:

    def __init__(self, source, target, graph, graphSize):
        self.source = source
        self.target = target
        self.graph = graph
        self.graphSize = graphSize

    def dijkstraRoute(self):
        m = self.graphSize 
        i = 0
        vert = 0
        k = 0
        newDist = 0
        minn = 0
        M = [0 for x in range(m)] #Determina se o vertice ja foi visitado
        L = [9999999999 for x in range(m)] #Infinito, determina o comprimento do caminho mais curto
        A = [-1 for x in range(m)] #Determina o caminho mais curto entre origem e destino
        route = []

        vert = self.source
        L[vert] = 0

        while(vert != self.target and vert != -1): #enquanto nao chegou no destino ou o caminho não for inexistente
            for i in range(m): #percorre os vertices adjacentes a vert
                if self.graph[vert][i] != 0 and M[i] == 0: #se existir aresta e ela nao foi visitada ainda
                    newDist = L[vert] + self.graph[vert][i] #pega o custo da aresta(vet, i) e soma ao comprimento existente
                    if (L[i]>newDist): #se o comprimento do vertice i for maior do que o calculado, atualiza o valor
                        L[i] = newDist
                        A[i] = vert
            M[vert] = 1 
            minn = 999999999
            vert = -1
            
            for i in range(m): #atuaiza o vertice da vez
                if M[i] == 0 and L[i] < minn:
                    minn = L[i]
                    vert = i
        
        if vert == self.target: #Pega o custo da origem até o destino
            cost = L[self.target]
            route.append(self.target) #Inclui o destino no caminho

            while vert != self.source: #Pega o caminho de trás pra frente
                route.append(A[vert])
                vert = A[vert]

            return (list(reversed(route)), cost)

        return None 

