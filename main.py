# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eda.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import networkx as nx

import networkx as nx
G1 = nx.Graph()
G2 = nx.Graph()

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtTest
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import queue
matplotlib.use('Qt5Agg')

'''class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        G.add_nodes_from(["B","A","C","D"])
        G.add_edges_from([('A','C'), ('B','D'), ('B','E'), ('C', 'E')])
        nx.draw(G, with_labels=True, font_weight='normal')
        fig = Figure(figsize=(width, height), dpi=dpi)
        plt.show()
        #self.axes = fig.add_subplot(111)
        fig = plt.figure()
        super(MplCanvas, self).__init__(fig)'''




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 440, 113, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 510, 113, 20))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 580, 141, 20))
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(744, 460, 101, 181))
        self.pushButton.setObjectName("pushButton")
        self.func1 = QtWidgets.QLineEdit(self.centralwidget)
        self.func1.setGeometry(QtCore.QRect(30, 460, 701, 31))
        self.func1.setObjectName("func1")
        self.result = QtWidgets.QLineEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(30, 610, 701, 31))
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.func2 = QtWidgets.QLineEdit(self.centralwidget)
        self.func2.setGeometry(QtCore.QRect(30, 530, 701, 31))
        self.func2.setObjectName("func2")

        self.image1 = QtWidgets.QLabel(self.centralwidget)
        self.image1.setGeometry(QtCore.QRect(30, 20, 391, 411))
        self.image1.setText("")
        self.image1.setPixmap(QtGui.QPixmap("Graph.png"))
        self.image1.setScaledContents(True)
        self.image1.setObjectName("image1")
        self.image2 = QtWidgets.QLabel(self.centralwidget)
        self.image2.setGeometry(QtCore.QRect(450, 20, 391, 411))
        self.image2.setText("")
        self.image2.setPixmap(QtGui.QPixmap("Graph.png"))
        self.image2.setScaledContents(True)
        self.image2.setObjectName("image2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "Boolean Function 1 :"))
        self.lineEdit_2.setText(_translate("MainWindow", "Boolean Function 2 :"))
        self.lineEdit_3.setText(_translate("MainWindow", "Resulting Boolean function"))
        self.pushButton.setText(_translate("MainWindow", "GO!"))
        self.pushButton.clicked.connect(lambda: self.go_clicked())

    def go_clicked(self):

        print(self.func1.text())
        print(self.func2.text())
        func1 = self.func1.text()
        func2 = self.func2.text()

        #parser function here
        #func1 hold the string written in bool function 1
        #func2 hold the string written in bool function 2

        #parser end


        #make the Graph here , what's written in this block is just a sample
        #sample of G1 and G2
        G1.add_nodes_from(["B", "A", "C", "D"])
        G1.add_edges_from([('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'E')])
        nx.draw(G1)
        plt.savefig("Graph1.png", format="PNG")
        self.image1.setPixmap(QtGui.QPixmap("Graph1.png"))

        G2.add_nodes_from(["Z", "X", "Y", "M"])
        G2.add_edges_from([('Z', 'X'), ('Y', 'M')])
        nx.draw(G2)
        plt.savefig("Graph2.png", format="PNG")
        self.image2.setPixmap(QtGui.QPixmap("Graph2.png"))
        #### sample end
        #### G1 and G2 are generated by you which is the ROBDD of function 1 , function 2
        #block end
        #



        #result text (result of ROBDD) as boolean function convert it to string and print it in result
        result = "trial result" #sample result
        self.result.setText(result)

        #result end


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
