import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QRadioButton, QPushButton, QPlainTextDocumentLayout

class Gui(QWidget):
    route = " "
    time = " "

    def getRoute(self):
        return self.route
    
    def setRoute(self, newRoute):
        self.route = newRoute

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Best Route')
        
        #Criação da label e do textEdit de origem
        origemLbl = QLabel('Origem:', self)
        origemLbl.move(20, 10)
        txtOrigem = QLineEdit(self)
        txtOrigem.move(20, 30)
        txtOrigem.resize(45, 25)

        #Criação da label e do textEdit de destino
        destinoLbl = QLabel('Destino:', self)
        destinoLbl.move(100, 10)
        txtDestino = QLineEdit(self)
        txtDestino.move(100, 30)
        txtDestino.resize(45, 25)

        #Criação dos radioButtons para escolha do algoritmo
        algoritmoDijk = QRadioButton('Dijkstra', self)
        algoritmoDijk.move(300, 20)
        algoritmoDijk.setChecked(True)

        algoritmoAS = QRadioButton('A*', self)
        algoritmoAS.move(300, 40)

        #Criação do botao de pesquisa
        btnPesquisar = QPushButton('Pesquisar', self)
        btnPesquisar.move(160, 80)

        #Criação da label time, mostra o tempo da pesquisa
        lblTime = QLabel('Tempo:', self)
        lblTime.move(300, 230)

        lblTimeResult = QLabel(self.time, self)
        lblTimeResult.move(350, 230)

        #Criação da label do resultado da melhor rota
        lblRouteResult = QLabel(self.route, self)
        #lblRouteResult.setText("textExample")
        lblRouteResult.setWordWrap(True)
        lblRouteResult.move(10, 110)
        lblRouteResult.resize(385, 100)

        self.show()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())