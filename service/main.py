from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QProgressDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
import requests
import sys

from implementacao import Consulta, extrair_produtos
from principal import Ui_MainWindow

class Worker(QThread):
    update_table = pyqtSignal(int, object)  # Sinal para atualizar a tabela

    def __init__(self, consulta):
        super().__init__()
        self.consulta = consulta

    def run(self):
        produtos = self.consulta.get_consulta()
        produtos_ordenados = self.consulta.ordenar_produtos(produtos)
        response = extrair_produtos(produtos_ordenados)
        
        for linha, produto in enumerate(response):
            self.update_table.emit(linha, produto)

class TelaPrincipal(QMainWindow):
    def __init__(self):
        super(TelaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Pesquisar.clicked.connect(self.pesquisar)
        self.ui.Limpar.clicked.connect(self.limpar)
        
        self.worker = None

    def limpar(self):
        self.ui.tabela_resultado.clearContents()
        self.ui.tabela_resultado.setRowCount(0)

    def atualizar_tabela(self, linha, produto):
        self.ui.tabela_resultado.insertRow(linha)
        self.ui.tabela_resultado.setRowHeight(linha, 70)
        
        for coluna in range(self.ui.tabela_resultado.columnCount()):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tabela_resultado.setItem(linha, coluna, item)
            
        self.ui.tabela_resultado.setItem(linha, 0, QTableWidgetItem(produto.title))
        self.ui.tabela_resultado.setItem(linha, 1, QTableWidgetItem(produto.price))
        self.ui.tabela_resultado.setItem(linha, 2, QTableWidgetItem(produto.story))
        
        url_imagem = produto.img.strip("'")
        
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
            pass

    def pesquisar(self):
    # Alterar o cursor para o ícone de espera durante a pesquisa
        self.setCursor(Qt.WaitCursor)

        # Limpa a tela antes de realizar a nova pesquisa
        self.limpar()
        
        # Obtém o texto de pesquisa
        pesquisa = self.ui.caixa_pesquisa.text()
        consulta = Consulta(pesquisa)
        
        # Cria e inicia o worker
        self.worker = Worker(consulta)
        self.worker.update_table.connect(self.atualizar_tabela)
        
        # Define as conexões para mostrar e esconder o cursor de espera
        self.worker.started.connect(lambda: self.setCursor(Qt.WaitCursor))
        self.worker.finished.connect(lambda: self.setCursor(Qt.ArrowCursor))
        
        self.worker.start()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec_())
