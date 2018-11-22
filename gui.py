from dijkstra import Dijkstra
from dataSet import DataSet
import time

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QRadioButton, QPushButton, QPlainTextDocumentLayout

class Gui(QWidget):

    def getRoute(self):
        return self.route
    
    def setRoute(self, newRoute):
        self.route = newRoute


    def __init__(self, dataSet):
        self.dataSet = dataSet
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Best Route')
        
        #Criação da label e do textEdit de origem
        origemLbl = QLabel('Origem:', self)
        origemLbl.move(20, 10)
        self.txtOrigem = QLineEdit(self)
        self.txtOrigem.move(20, 30)
        self.txtOrigem.resize(45, 25)

        #Criação da label e do textEdit de destino
        destinoLbl = QLabel('Destino:', self)
        destinoLbl.move(100, 10)
        self.txtDestino = QLineEdit(self)
        self.txtDestino.move(100, 30)
        self.txtDestino.resize(45, 25)

        #Criação dos radioButtons para escolha do algoritmo
        self.algoritmoDijk = QRadioButton('Dijkstra', self)
        self.algoritmoDijk.move(300, 20)
        self.algoritmoDijk.setChecked(True)

        self.algoritmoAS = QRadioButton('A*', self)
        self.algoritmoAS.move(300, 40)

        #Criação do botao de pesquisa
        self.btnPesquisar = QPushButton('Pesquisar', self)
        self.btnPesquisar.move(160, 80)
        self.btnPesquisar.clicked.connect(self.btn_pesquisarClicked)

        #Criação da label time, mostra o tempo da pesquisa
        self.lblTime = QLabel('Tempo:', self)
        self.lblTime.move(260, 230)

        self.lblTimeResult = QLabel(" ", self)
        self.lblTimeResult.move(310, 230)
        self.lblTimeResult.resize(100, 15)

        #Criação da label de custo medio, mostra o custo medio da viagem
        self.lblCusto = QLabel('Custo médio:', self)
        self.lblCusto.move(10, 230)

        self.lblCustoResult = QLabel(" ", self)
        self.lblCustoResult.move(90, 230)
        self.lblCustoResult.resize(100, 15)


        #Criação da label do resultado da melhor rota
        self.lblRouteResult = QLabel(" ", self)
        self.lblRouteResult.setWordWrap(True)
        self.lblRouteResult.move(10, 110)
        self.lblRouteResult.resize(385, 100)

        self.show()
    
    def btn_pesquisarClicked(self):
        origem = self.txtOrigem.text().upper()
        destino = self.txtDestino.text().upper()
        validation = True
        states = self.dataSet.getStates()
        if(origem == "" or destino == ""):
            self.lblRouteResult.setText("Por favor, preencha todos os campos!")
            self.lblCustoResult.clear()
            self.lblTimeResult.clear()
            validation = False
        
        elif(origem not in states or destino not in states):
            self.lblRouteResult.setText("Por favor, preencha todos os campos de forma válida!")
            self.lblCustoResult.clear()
            self.lblTimeResult.clear()
            validation = False
        
        if(self.algoritmoDijk.isChecked() and validation):            
            origem = self.dataSet.rotuleToRepresentation(origem)
            destino = self.dataSet.rotuleToRepresentation(destino)

            dijkstra = Dijkstra(origem, destino, self.dataSet.getDataSet())
            
            #Calculando a melhor rota e pegando o tempo de execução e o custo da viagem
            firstTime = time.time()
            bestroute = dijkstra.dijkstraRoute()
            lastTime = time.time()
            timeOfExecution = lastTime - firstTime
            self.lblTimeResult.setText(('{:.5f}'.format(timeOfExecution)) + " ms")
            
            if(bestroute is not None):
                #Indicando o custo medio da viagem
                self.lblCustoResult.setText("R$ " + '{:.2F}'.format(bestroute[1]))
                
                #Indicando a melhor rota para o trajeto
                bestRouteRotuled = []
                for r in bestroute[0]:
                    if(not (r == bestroute[0][-1])):
                        bestRouteRotuled.append(self.dataSet.rotuleToRepresentation(r) + ' \u2B95 ')
                    else:
                        bestRouteRotuled.append(self.dataSet.rotuleToRepresentation(r))
                self.lblRouteResult.setText(' '.join(bestRouteRotuled))
            else:
                self.lblCustoResult.setText("R$ 0")
                self.lblRouteResult.setText("Não foi possível encontrar uma rota.")

if __name__ == '__main__':
    dataSet = DataSet('./dataSet.csv')
    app = QApplication(sys.argv)
    gui = Gui(dataSet)
    sys.exit(app.exec_())
