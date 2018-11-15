from dataSet import DataSet

class Dijkstra:

    def __init__(self, source, destination, graph):
        self.source = source
        self.destination = destination
        self.graph = graph

    def dijkstraRoute(self):
        m = 9 #alterar o tamanho da matriz quando colocarmos todo o dataset
        i = 0
        vert = 0
        k = 0
        newDist = 0
        minn = 0
        M = [0 for x in range(m)]
        L = [99999 for x in range(m)]
        A = [-1 for x in range(m)]
        route = []

        vert = self.source
        L[vert] = 0

        while(vert != self.destination and vert != -1):
            for i in range(m):
                if self.graph[vert][i] != 0 and M[i] == 0:
                    newDist = L[vert] + self.graph[vert][i]
                    if (newDist < L[i]):
                        L[i] = newDist
                        A[i] = vert
            M[vert] = 1
            minn = 99999
            vert = -1
            
            for i in range(m):
                if M[i] == 0 and L[i] < minn:
                    minn = L[i]
                    vert = i
        
        if vert == self.destination:
            cost = L[self.destination]
            route.append(self.destination)

            while vert != self.source:
                route.append(A[vert])
                vert = A[vert]

            return (list(reversed(route)), cost)

        return None #Quando nao for possivel encontrar uma rota, é retornado nulo

'''
def main():
    dataSet = DataSet('./datasetNordeste.csv')
    dijkstra = Dijkstra(1, 7, dataSet.getDataSet())

    print(dijkstra.dijkstraRoute())
    #print(lista)
main()
'''