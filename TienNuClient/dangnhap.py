# Form implementation generated from reading ui file 'dangnhap.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from functools import partial
from PyQt6 import QtCore, QtGui, QtWidgets
import demo
import baihat
userID=""
from GetDataFromServer import GetDataFromServer
client = GetDataFromServer()
client.connect()

class dangnhap(object):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 206)
        self.lblTitle = QtWidgets.QLabel(parent=Form)
        self.lblTitle.setGeometry(QtCore.QRect(110, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblUsername = QtWidgets.QLabel(parent=Form)
        self.lblUsername.setGeometry(QtCore.QRect(30, 70, 61, 16))
        self.lblUsername.setObjectName("lblUsername")
        self.lblPassword = QtWidgets.QLabel(parent=Form)
        self.lblPassword.setGeometry(QtCore.QRect(30, 110, 51, 16))
        self.lblPassword.setObjectName("lblPassword")
        self.txtUsername = QtWidgets.QLineEdit(parent=Form)
        self.txtUsername.setGeometry(QtCore.QRect(100, 70, 231, 22))
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(parent=Form)
        self.txtPassword.setGeometry(QtCore.QRect(100, 110, 231, 22))
        self.txtPassword.setObjectName("txtPassword")

        dm = demo.demo()
        lstUser =[]
        lst = client.sendSignal("GET_USER_LIST")
        for user in lst:
            lstUser.append(user['username'])
        print(lstUser)


        self.btnDangNhap = QtWidgets.QPushButton(parent=Form)
        self.btnDangNhap.setGeometry(QtCore.QRect(60, 160, 75, 24))
        self.btnDangNhap.setObjectName("btnDangNhap")
        self.btnDangNhap.clicked.connect(lambda: self.ValidUser(self.txtUsername.text(),self.txtPassword.text(),lst,dm))

        self.btnDangKy = QtWidgets.QPushButton(parent=Form)
        self.btnDangKy.setGeometry(QtCore.QRect(250, 160, 75, 24))
        self.btnDangKy.setStyleSheet("color: rgb(0, 0, 255);")
        self.btnDangKy.setObjectName("btnDangKy")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblTitle.setText(_translate("Form", "ĐĂNG NHẬP"))
        self.lblUsername.setText(_translate("Form", "Username"))
        self.lblPassword.setText(_translate("Form", "Password"))
        self.btnDangNhap.setText(_translate("Form", "Đăng nhập"))
        self.btnDangKy.setText(_translate("Form", "Đăng ký"))

    def ValidUser(self,username,password,lst,dm):
        
        # global userID
        for user in lst:
            if((str(username)==str(user['username']) )and (str(password)==str(user['password']))):
                userID=str(user['username'])
                # print(userIDdemo)
                dm.setUserID(user['username'])
                dm.show()
                self.tat()
                return userID
                

    def tat(self):
        Form.close()
        # dm.show()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = dangnhap()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
