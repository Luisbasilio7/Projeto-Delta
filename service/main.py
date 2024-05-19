from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import QTableWidgetItem
import requests
import os,sys

from implementacao import Consulta
from implementacao import extrair_produtos
from principal import Ui_MainWindow

class telaPrincipal(QMainWindow):
    def __init__(self):
        super(telaPrincipal,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Pesquisar.clicked.connect(self.pesquisar)
        self.ui.Limpar.clicked.connect(self.limpar)
        



    def pesquisar(self):
        pesquisa = self.ui.caixa_pesquisa.text()
        consulta = Consulta(pesquisa)
        produtos = consulta.get_consulta()
        produtos_ordenados = consulta.ordenar_produtos(produtos)
        response = extrair_produtos(produtos_ordenados)
        
        self.ui.tabela_resultado.setRowCount(0)
        for linha, produto in enumerate(response):
            self.ui.tabela_resultado.insertRow(linha)
            self.ui.tabela_resultado.setItem(linha, 0, QTableWidgetItem(produto.title))
            self.ui.tabela_resultado.setItem(linha, 1, QTableWidgetItem(produto.price))
            self.ui.tabela_resultado.setItem(linha, 2, QTableWidgetItem(produto.story))
            
            url_imagem = produto.img.strip("'")
            
            # Tentar carregar a imagem apenas se a URL for válida
            try:
                imagem = QLabel()
                largura = 50
                altura = 50
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(url_imagem).content)  # Carregar imagem do URL
                pixmap = pixmap.scaled(largura, altura)  # Redimensionar imagem se necessário
                imagem.setPixmap(pixmap)
                self.ui.tabela_resultado.setCellWidget(linha, 3, imagem)
            except Exception as e:

                continue
        altura_tab = 50 
        num_linhas = self.ui.tabela_resultado.rowCount()
        for linha in range(num_linhas):
            self.ui.tabela_resultado.setRowHeight(linha, altura_tab)


    def limpar(self):
        limpar = self

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaPrincipal()
    window.show()
    sys.exit(app.exec_())    