import numpy
import csv
class DataSet:

    def __init__(self, file):
        self.file = file
        self.dataSet = [[99999]*9 for i in range(9)] #Limitado aos estados do nordeste (lembrar de atualizar para todos os estados brasileiros)
        self.verticeState = {
            0: "RN",
            1: "PE",
            2: "BA",
            3: "PI",
            4: "MA",
            5: "CE",
            6: "SE",
            7: "AL",
            8: "PB",
            9: "AC",
            10: "AP",
            11: "AM",
            12: "DF",
            13: "ES",
            14: "GO",
            15: "MT",
            16: "MS",
            17: "MG",
            18: "PA",
            19: "PR",
            20: "RJ",
            21: "RS",
            22: "RO", 
            23: "RR",
            24: "SC",
            25: "SP",
            26: "TO"
        }
        self.loadCSV()

    def loadCSV(self): #Carrega o CSV em forma de uma lista de listas
        with open(self.file) as f:
            data = [list(line) for line in csv.reader(f)]
            newData = self.allRotuleToRepresentation(data)
        cont = 0
        for d in newData:
            cont = cont+1
            self.dataSet[int(d[0])][int(d[1])] = float(d[2])
    def getDataSet(self): #Retorna o data set ja em forma de matriz
        return self.dataSet

    def allRotuleToRepresentation(self, data): #Converta os rotulos em numeros para cada vertice
        for d in data:
            for representation, rotule in self.verticeState.items():
                if rotule == d[0]:
                    d[0] = str(representation)
                if rotule == d[1]:
                    d[1] = str(representation)        
        return data
        
if __name__ == '__main__':
    dataSet = DataSet('./datasetNordeste.csv')
    print(dataSet.getDataSet())