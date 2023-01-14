from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_IFCalc(object):
    def setupUi(self, IFCalc):
        IFCalc.setObjectName("IFCalc")
        IFCalc.resize(443, 541)
        IFCalc.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(IFCalc)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(90, 0, 241, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.aviso = QtWidgets.QLabel(self.centralwidget)
        self.aviso.setGeometry(QtCore.QRect(10, 150, 431, 16))
        self.aviso.setObjectName("aviso")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(140, 110, 171, 41))
        self.titulo.setObjectName("titulo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 180, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 270, 151, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 300, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 460, 251, 16))
        self.label_6.setObjectName("label_6")
        self.num_bimestres = QtWidgets.QComboBox(self.centralwidget)
        self.num_bimestres.setGeometry(QtCore.QRect(250, 180, 69, 22))
        self.num_bimestres.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.num_bimestres.setObjectName("num_bimestres")
        self.num_bimestres.addItem("")
        self.num_bimestres.addItem("")
        self.campo_media1 = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_media1.setGeometry(QtCore.QRect(250, 210, 113, 20))
        self.campo_media1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.campo_media1.setObjectName("campo_media1")
        self.campo_media2 = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_media2.setGeometry(QtCore.QRect(250, 240, 113, 20))
        self.campo_media2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.campo_media2.setObjectName("campo_media2")
        self.campo_media3 = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_media3.setGeometry(QtCore.QRect(250, 270, 113, 20))
        self.campo_media3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.campo_media3.setObjectName("campo_media3")
        self.campo_media4 = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_media4.setGeometry(QtCore.QRect(250, 300, 113, 20))
        self.campo_media4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.campo_media4.setObjectName("campo_media4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 400, 141, 16))
        self.label_7.setStyleSheet("color: rgb(104, 185, 46);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 430, 171, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 340, 191, 16))
        self.label_9.setObjectName("label_9")
        self.botao_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.botao_calcular.setGeometry(QtCore.QRect(180, 340, 81, 31))
        self.botao_calcular.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_calcular.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.botao_calcular.setObjectName("botao_calcular")
        self.campo_mediafinal = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_mediafinal.setGeometry(QtCore.QRect(250, 400, 113, 20))
        self.campo_mediafinal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.campo_mediafinal.setObjectName("campo_mediafinal")
        self.campo_situacao = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_situacao.setGeometry(QtCore.QRect(250, 430, 113, 20))
        self.campo_situacao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.campo_situacao.setObjectName("campo_situacao")
        self.campo_notafinal = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_notafinal.setGeometry(QtCore.QRect(270, 460, 113, 20))
        self.campo_notafinal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.campo_notafinal.setObjectName("campo_notafinal")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(260, 340, 191, 16))
        self.label_10.setObjectName("label_10")
        self.botao_sobre = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sobre.setGeometry(QtCore.QRect(50, 500, 75, 23))
        self.botao_sobre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sobre.setStyleSheet("background-color: rgb(104, 185, 46);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.botao_sobre.setObjectName("botao_sobre")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(310, 500, 75, 23))
        self.botao_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(104, 185, 46);")
        self.botao_sair.setObjectName("botao_sair")
        IFCalc.setCentralWidget(self.centralwidget)

        #remover opção de maximizar tela
        IFCalc.setFixedSize(IFCalc.width(), IFCalc.height())

        self.retranslateUi(IFCalc)
        self.botao_sair.clicked.connect(IFCalc.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(IFCalc)

        #combo box, modificar
        self.campo_media3.setEnabled(False)
        self.campo_media4.setEnabled(False)
        self.num_bimestres.currentIndexChanged.connect(self.modificar_campos)

        #botão calcular
        self.botao_calcular.clicked.connect(self.calcular)

        #botão sobre
        self.botao_sobre.clicked.connect(self.mostrar_sobre)

    def mostrar_sobre(self):
        from sobre import Ui_sobre
        self.janela = QtWidgets.QMainWindow()
        self.sobre = Ui_sobre()
        self.sobre.setupUi(self.janela)
        self.janela.show()

    def modificar_campos(self):
        if int(self.num_bimestres.currentText()) == 2:
            self.campo_media3.setEnabled(False)
            self.campo_media4.setEnabled(False)
        else:
            self.campo_media3.setEnabled(True)
            self.campo_media4.setEnabled(True)

    def calcular(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")

        op = int(self.num_bimestres.currentText())
        if op == 2:
            try:
                num1 = int(self.campo_media1.text())
                num2 = int(self.campo_media2.text())
                media = int((num1 * 2 + num2 * 3) / 5)
                self.campo_mediafinal.setText(str(media))

                if media >= 60:
                    self.campo_situacao.setText("Aprovado!")
                elif media < 40:
                    self.campo_situacao.setText("Reprovado")
                else:
                    self.campo_situacao.setText("Em recuperação")

                if media > 39 and media < 60:
                    notafinal = 120 - media
                    #Quanto precisa na prova final:
                    self.campo_notafinal.setText(str(notafinal))
                else:
                    self.campo_notafinal.setText("")

            except ValueError:
                msg.setText("Números incorretos!")
                msg.exec()
        else:
            try:
                num1 = int(self.campo_media1.text())
                num2 = int(self.campo_media2.text())
                num3 = int(self.campo_media3.text())
                num4 = int(self.campo_media4.text())
                media = int((num1 * 2 + num2 * 2 + num3 * 3 + num4 * 3) / 10)
                self.campo_mediafinal.setText(str(media))

                if media >= 60:
                    self.campo_situacao.setText("Aprovado!")
                elif media < 40:
                    self.campo_situacao.setText("Reprovado")
                else:
                    self.campo_situacao.setText("Em recuperação")

                if media > 39 and media < 60:
                    notafinal = 120 - media
                    # Quanto precisa na prova final:
                    self.campo_notafinal.setText(str(notafinal))
                else:
                    self.campo_notafinal.setText("")

            except ValueError:
                msg.setText("Números incorretos!")
                msg.exec()

    def retranslateUi(self, IFCalc):
        _translate = QtCore.QCoreApplication.translate
        IFCalc.setWindowTitle(_translate("IFCalc", "MainWindow"))
        self.aviso.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">As médias devem ser inseridas utilizando a notação de 0 a 100</span></p></body></html>"))
        self.titulo.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#aa0000;\">Calculadora IFRN</span></p></body></html>"))
        self.label.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Quantidade de bimestres:</span></p></body></html>"))
        self.label_2.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Média do 1° bimestre:</span></p></body></html>"))
        self.label_3.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Média do 2° bimestre:</span></p></body></html>"))
        self.label_4.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Média do 3° bimestre:</span></p></body></html>"))
        self.label_5.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Média do 4° bimestre:</span></p></body></html>"))
        self.label_6.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#66b62d;\">Nota necessária para prova final: </span></p></body></html>"))
        self.num_bimestres.setItemText(0, _translate("IFCalc", "2"))
        self.num_bimestres.setItemText(1, _translate("IFCalc", "4"))
        self.label_7.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#589d27;\">Média final:</span></p></body></html>"))
        self.label_8.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#66b52d;\">Situação do aluno: </span></p></body></html>"))
        self.label_9.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">=-=-=-=-=-=-=-=</span></p></body></html>"))
        self.botao_calcular.setText(_translate("IFCalc", "Calcular"))
        self.label_10.setText(_translate("IFCalc", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">=-=-=-=-=-=-=-=</span></p></body></html>"))
        self.botao_sobre.setText(_translate("IFCalc", "Sobre"))
        self.botao_sair.setText(_translate("IFCalc", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IFCalc = QtWidgets.QMainWindow()
    ui = Ui_IFCalc()
    ui.setupUi(IFCalc)
    IFCalc.show()
    sys.exit(app.exec_())
