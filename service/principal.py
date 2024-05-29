# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 496)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:0.596, x2:0.489, y2:0, stop:0 rgba(8, 68, 93, 255), stop:1 rgba(21, 136, 220, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 261, 71))
        self.label.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("image: url(:/icons/PriceHub.png);\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.653, x2:0.506, y2:0.0284091, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(80, 182, 255, 0));\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.Pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.Pesquisar.setGeometry(QtCore.QRect(640, 110, 81, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.5, 0.596, 0.489, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(8, 68, 93))
        gradient.setColorAt(1.0, QtGui.QColor(21, 136, 220))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.5, 0.596, 0.489, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(8, 68, 93))
        gradient.setColorAt(1.0, QtGui.QColor(21, 136, 220))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.5, 0.596, 0.489, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(8, 68, 93))
        gradient.setColorAt(1.0, QtGui.QColor(21, 136, 220))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.5, 0.596, 0.489, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(8, 68, 93))
        gradient.setColorAt(1.0, QtGui.QColor(21, 136, 220))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.5, 0.596, 0.489, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(8, 68, 93))
        gradient.setColorAt(1.0, QtGui.QColor(21, 136, 220))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.5, 0.596, 0.489, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(8, 68, 93))
        gradient.setColorAt(1.0, QtGui.QColor(21, 136, 220))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.5, 0.596, 0.489, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(8, 68, 93))
        gradient.setColorAt(1.0, QtGui.QColor(21, 136, 220))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.5, 0.596, 0.489, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(8, 68, 93))
        gradient.setColorAt(1.0, QtGui.QColor(21, 136, 220))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.5, 0.596, 0.489, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(8, 68, 93))
        gradient.setColorAt(1.0, QtGui.QColor(21, 136, 220))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Pesquisar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Pesquisar.setFont(font)
        self.Pesquisar.setMouseTracking(False)
        self.Pesquisar.setAutoFillBackground(False)
        self.Pesquisar.setStyleSheet("color: rgb(255, 255, 255);")
        self.Pesquisar.setObjectName("Pesquisar")
        self.Limpar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpar.setGeometry(QtCore.QRect(640, 160, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Limpar.setFont(font)
        self.Limpar.setStyleSheet("color: rgb(255, 255, 255);")
        self.Limpar.setObjectName("Limpar")
        self.caixa_pesquisa = QtWidgets.QLineEdit(self.centralwidget)
        self.caixa_pesquisa.setGeometry(QtCore.QRect(30, 110, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.caixa_pesquisa.setFont(font)
        self.caixa_pesquisa.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.caixa_pesquisa.setToolTipDuration(-1)
        self.caixa_pesquisa.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.caixa_pesquisa.setText("")
        self.caixa_pesquisa.setAlignment(QtCore.Qt.AlignCenter)
        self.caixa_pesquisa.setObjectName("caixa_pesquisa")
        self.tabela_resultado = QtWidgets.QTableWidget(self.centralwidget)
        self.tabela_resultado.setGeometry(QtCore.QRect(30, 170, 581, 301))
        self.tabela_resultado.setMinimumSize(QtCore.QSize(0, 281))
        self.tabela_resultado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(8, 8, 8);")
        self.tabela_resultado.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabela_resultado.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabela_resultado.setAutoScroll(False)
        self.tabela_resultado.setAutoScrollMargin(20)
        self.tabela_resultado.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tabela_resultado.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tabela_resultado.setTextElideMode(QtCore.Qt.ElideNone)
        self.tabela_resultado.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tabela_resultado.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tabela_resultado.setShowGrid(True)
        self.tabela_resultado.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_resultado.setWordWrap(True)
        self.tabela_resultado.setCornerButtonEnabled(True)
        self.tabela_resultado.setRowCount(0)
        self.tabela_resultado.setColumnCount(5)
        self.tabela_resultado.setObjectName("tabela_resultado")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabela_resultado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabela_resultado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabela_resultado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabela_resultado.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabela_resultado.setHorizontalHeaderItem(4, item)
        self.tabela_resultado.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_resultado.horizontalHeader().setSortIndicatorShown(False)
        self.tabela_resultado.verticalHeader().setSortIndicatorShown(False)
        # Definir tamanho das colunas 
        self.tabela_resultado.setColumnWidth(0, 170)
        self.tabela_resultado.setColumnWidth(1, 130)
        self.tabela_resultado.setColumnWidth(2, 130)
        self.tabela_resultado.setColumnWidth(3, 130)
        self.tabela_resultado.setColumnWidth(4, 0)
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PriceHub"))
        self.Pesquisar.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Pesquisar.setText(_translate("MainWindow", "Pesquisar"))
        self.Limpar.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Limpar.setText(_translate("MainWindow", "Limpar"))
        self.caixa_pesquisa.setPlaceholderText(_translate("MainWindow", "Digite o modelo do aparelho que deseja consultar "))
        self.tabela_resultado.setSortingEnabled(False)
        # item = self.tabela_resultado.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "Itens"))
        item = self.tabela_resultado.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Modelo "))
        
        item = self.tabela_resultado.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Preço"))
        
        item = self.tabela_resultado.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Loja"))
        
        item = self.tabela_resultado.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Imagem"))
        
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
