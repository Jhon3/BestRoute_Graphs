#vertex should start with zero
#if you are giving weight above 999 adjust min in program
#result will be the shortest path and the distace to each vertex from source vertex in order





def dijkstra(matrix,m,n):
    origem = 0
    dest = 3

    i = 0
    vert = 0
    k = 0
    novaDist = 0
    minimo = 0
    M = [0 for x in range(m)]
    L = [99999 for x in range(m)]
    A = [-1 for x in range(m)]
    caminho = []

    vert = origem
    L[vert] = 0

    while(vert != dest and vert != -1):
        for i in range(m):
            if matrix[vert][i] != 0 and M[i] == 0:
                novaDist = L[vert] + matrix[vert][i]
                if (novaDist < L[i]):
                    L[i] = novaDist
                    A[i] = vert
        M[vert] = 1
        minimo = 99999
        vert = -1
        
        for i in range(m):
            if M[i] == 0 and L[i] < minimo:
                minimo = L[i]
                vert = i
    
    if vert == dest:
        print("Comprimento entre origem e destino",L[dest])
        caminho.append(dest)

        while vert != origem:
            caminho.append(A[vert])
            vert = A[vert]

        print(caminho)

    
def main():
    print("Dijkstras algorithum graph using matrix representation \n")
    n=int(input("number of elements in row"))
    m=int(input("number of elements in column"))
    #print("enter the values of the matrix")
    matrix=[[0 for x in range(m)] for x in range(n)]
    for i in range (n):
        for j in range (m):
            matrix[i][j]=int(input("enter the values of the matrix"))
    print(matrix)
    dijkstra(matrix,n,m)
main()