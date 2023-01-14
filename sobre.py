from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sobre(object):
    def setupUi(self, sobre):
        sobre.setObjectName("sobre")
        sobre.resize(422, 285)
        sobre.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(sobre)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 0, 241, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 281, 31))
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 190, 81, 16))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.botao_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltar.setGeometry(QtCore.QRect(170, 240, 81, 23))
        self.botao_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_voltar.setStyleSheet("background-color: rgb(104, 185, 46);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.botao_voltar.setObjectName("botao_voltar")
        self.botao_voltar.clicked.connect(sobre.close)
        sobre.setCentralWidget(self.centralwidget)

        self.retranslateUi(sobre)
        QtCore.QMetaObject.connectSlotsByName(sobre)

    def retranslateUi(self, sobre):
        _translate = QtCore.QCoreApplication.translate
        sobre.setWindowTitle(_translate("sobre", "Sobre"))
        self.label_2.setText(_translate("sobre", "Desenvolvido por Cláudia Raiane"))
        self.label_3.setText(_translate("sobre", "Versão 1.0"))
        self.botao_voltar.setText(_translate("sobre", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sobre = QtWidgets.QMainWindow()
    ui = Ui_sobre()
    ui.setupUi(sobre)
    sobre.show()
    sys.exit(app.exec_())
