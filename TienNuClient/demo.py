# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QVBoxLayout,QSizePolicy
from PyQt6.QtWidgets import *
import baihat
import NhacBUS
import playlist_GUI
import Favorite_Gui
import taikhoancanhan
from GetDataFromServer import GetDataFromServer
# userIDDemo=""

class demo(QMainWindow):
    userIDDemo=""
    userPassword=""
    name=""
    lstMusic=[]
    def __init__(self):
                super().__init__()
                self.setupUi()
 
    def setupUi(self):
        
       
        self.resize(812, 591)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("TienNuClient/imgs/chidep.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.menuPanel = QtWidgets.QFrame(parent=self.centralwidget)
        self.menuPanel.setGeometry(QtCore.QRect(0, 0, 201, 591))
        self.menuPanel.setStyleSheet("background-color: #092635;")
        self.menuPanel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menuPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menuPanel.setObjectName("menuPanel")
        self.appName = QtWidgets.QLabel(parent=self.menuPanel)
        self.appName.setGeometry(QtCore.QRect(60, 30, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        self.appName.setFont(font)
        self.appName.setStyleSheet("color: #9EC8B9;")
        self.appName.setObjectName("appName")
        self.txtSearch = QtWidgets.QLineEdit(parent=self.menuPanel)
        self.txtSearch.setGeometry(QtCore.QRect(30, 90, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.txtSearch.setFont(font)
        self.txtSearch.setStyleSheet("background-color: #9EC8B9;")
        self.txtSearch.setObjectName("txtSearch")
        self.btnFind = QtWidgets.QPushButton(parent=self.menuPanel)
        self.btnFind.setGeometry(QtCore.QRect(180, 90, 21, 21))
        self.btnFind.setText("")
        self.btnFind.setStyleSheet("background-color: white;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("TienNuClient/imgs/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnFind.setIcon(icon3)
        self.btnFind.setObjectName("btnFind")
        self.cbFind = QtWidgets.QComboBox(parent=self.menuPanel)
        self.cbFind.setGeometry(QtCore.QRect(30, 60, 171, 22))
        self.cbFind.setObjectName("cbFind")
        self.cbFind.addItem("All")
        self.cbFind.addItem("Songs name")
        self.cbFind.addItem("Artist")
        self.cbFind.setStyleSheet("background-color: white;")

        self.btnTrangChu = QtWidgets.QPushButton(parent=self.menuPanel)
        self.btnTrangChu.setGeometry(QtCore.QRect(20, 130, 151, 28))
        self.btnTrangChu.clicked.connect(self.toTrangchu)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btnTrangChu.setFont(font)
        self.btnTrangChu.setStyleSheet("color: #9EC8B9;")
        self.btnTrangChu.setObjectName("btnTrangChu")
        self.btnPlayList = QtWidgets.QPushButton(parent=self.menuPanel)
        self.btnPlayList.setGeometry(QtCore.QRect(20, 180, 151, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btnPlayList.setFont(font)
        self.btnPlayList.setStyleSheet("color: #9EC8B9;")
        self.btnPlayList.setObjectName("btnPlayList")
        self.btnPlayList.clicked.connect(self.toPlaylist)
        self.btnYeuThich = QtWidgets.QPushButton(parent=self.menuPanel)
        self.btnYeuThich.setGeometry(QtCore.QRect(20, 230, 151, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btnYeuThich.setFont(font)
        self.btnYeuThich.setStyleSheet("color: #9EC8B9;")
        self.btnYeuThich.setObjectName("btnYeuThich")
        self.btnYeuThich.clicked.connect(self.toFavorite)
        self.label = QtWidgets.QLabel(parent=self.menuPanel)
        self.label.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("TienNuClient/imgs/chidep-icon.jpg"))
        self.label.setObjectName("label")
        self.btnTaiKhoan = QtWidgets.QPushButton(parent=self.menuPanel)
        self.btnTaiKhoan.setGeometry(QtCore.QRect(20, 280, 151, 28))
        self.btnTaiKhoan.clicked.connect(self.toTaiKhoan)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btnTaiKhoan.setFont(font)
        self.btnTaiKhoan.setStyleSheet("color: #9EC8B9;")
        self.btnTaiKhoan.setObjectName("btnTaiKhoan")
        
        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(200, 0, 611, 591))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        

        
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setFixedWidth(611)
        self.scrollAreaWidgetContents.setFixedHeight(591)
        
        self.scrollAreaWidgetContents.setLayout(self.layout)
    
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.setCentralWidget(self.centralwidget)
        self.btnFind.clicked.connect(self.searchData)
        self.txtSearch.returnPressed.connect(self.searchData)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Chị Đẹp MP3"))
        self.appName.setText(_translate("MainWindow", "Chị Đẹp MP3"))
        self.btnTrangChu.setText(_translate("MainWindow", "Trang chủ"))
        self.btnPlayList.setText(_translate("MainWindow", "PlayList"))
        self.btnYeuThich.setText(_translate("MainWindow", "Yêu thích"))
        self.btnTaiKhoan.setText(_translate("MainWindow", "Tài khoản cá nhân"))

    def addDataToWidget(self,lstMusic):
        row=0
        for music in lstMusic:
            self.baihat=baihat.baihat(str(music["id"]),str(music["name"]),str(music["artist"]),str(music["luotNghe"]),str(music["img"]),music["mp3"],self.userIDDemo)
            print(self.userIDDemo)
            self.layout.addWidget(self.baihat,row,0)
            row+=1
        self.scrollAreaWidgetContents.setFixedHeight(80*(row+1))
        
    def clearWidget(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def searchData(self):
        item = self.cbFind.currentIndex()
        data = self.txtSearch.text()

        lstFound = []
        for music in self.lstMusic:
            if item == 0: #Tim theo id
                lstFound=self.lstMusic
            elif item == 1:#Tim theo ten nhac
                if data.lower() in str(music["name"]).lower():
                    lstFound.append(music)
            else:#Tim theo ten tac gia
                if data.lower() in str(music["artist"]).lower():
                    lstFound.append(music)
        self.clearWidget()
        self.addDataToWidget(lstFound)
        # self.addDataToTable(lstFound)
    
    def setUserID(self, userID):

        self.userIDDemo=userID
        client = GetDataFromServer()
        client.connect()
        self.lstMusic = client.sendSignal("GET_MUSIC_LIST")
        self.addDataToWidget(self.lstMusic)

    def setPassword(self,passw):
        self.userPassword=passw
       
    def setName(self,name):
        self.name=name


    def toPlaylist(self):
        self.playlist_GUI = playlist_GUI.playlist_GUI(self.userIDDemo)
        self.playlist_GUI.setObjectName("playlist_GUI")
        self.scrollArea.setWidget(self.playlist_GUI)
    def toFavorite(self):
        self.Favorite_Gui = Favorite_Gui.Favorite_GUI(self.userIDDemo)
        self.Favorite_Gui.setObjectName("Favorite_Gui")
        self.scrollArea.setWidget(self.Favorite_Gui)
    def toTaiKhoan(self):
        self.taikhoancanhan = taikhoancanhan.taikhoancanhan(self.userIDDemo,self.userPassword,self.name)
        self.taikhoancanhan.setObjectName("taikhoan_GUI")
        self.scrollArea.setWidget(self.taikhoancanhan)
    def toTrangchu(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setFixedWidth(611)
        self.scrollAreaWidgetContents.setFixedHeight(591)
        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.scrollAreaWidgetContents.setLayout(self.layout)
        client = GetDataFromServer()
        client.connect()
        lstMusic = client.sendSignal("GET_MUSIC_LIST")
        self.addDataToWidget(lstMusic)
        self.scrollAreaWidgetContents.setLayout(self.layout)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = demo()
    ui.show()
    
    sys.exit(app.exec())