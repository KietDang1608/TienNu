# Form implementation generated from reading ui file 'trangchu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 130, 600))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.widget.setObjectName("widget")
        self.btnMusic = QtWidgets.QPushButton(parent=self.widget)
        self.btnMusic.setGeometry(QtCore.QRect(10, 210, 110, 30))
        self.btnMusic.setStyleSheet("background-color: rgb(135, 133, 162);\n"
"color: rgb(255, 255, 255);")
        self.btnMusic.setObjectName("btnMusic")
        self.btnCategory = QtWidgets.QPushButton(parent=self.widget)
        self.btnCategory.setGeometry(QtCore.QRect(10, 260, 110, 30))
        self.btnCategory.setStyleSheet("background-color: rgb(135, 133, 162);\n"
"color: rgb(255, 255, 255);")
        self.btnCategory.setObjectName("btnCategory")
        self.btnPlayList = QtWidgets.QPushButton(parent=self.widget)
        self.btnPlayList.setGeometry(QtCore.QRect(10, 310, 110, 30))
        self.btnPlayList.setStyleSheet("background-color: rgb(135, 133, 162);\n"
"color: rgb(255, 255, 255);")
        self.btnPlayList.setObjectName("btnPlayList")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(130, 0, 670, 50))
        self.widget_2.setStyleSheet("background-color: rgb(135, 133, 162);")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(310, 20, 131, 16))
        self.label_5.setObjectName("label_5")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(130, 50, 670, 550))
        self.widget_3.setStyleSheet("\n"
"background-color: rgb(246, 246, 246);")
        self.widget_3.setObjectName("widget_3")
        self.frame = QtWidgets.QFrame(parent=self.widget_3)
        self.frame.setGeometry(QtCore.QRect(10, 20, 641, 191))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 41, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 113, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 113, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 70, 113, 22))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 100, 113, 22))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widget_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 230, 641, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnMusic.setText(_translate("MainWindow", "Music"))
        self.btnCategory.setText(_translate("MainWindow", "Categories"))
        self.btnPlayList.setText(_translate("MainWindow", "Playlist"))
        self.label_5.setText(_translate("MainWindow", "MUSIC"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "CATEGORY"))
        self.label_3.setText(_translate("MainWindow", "NAME"))
        self.label_4.setText(_translate("MainWindow", "ARTIST"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())