# Form implementation generated from reading ui file 'playlist-baihat.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import pygame
import baihat
import baihat1
from GetDataFromServer import GetDataFromServer

class Ui_Form(QWidget):
    def __init__(self,id,TenPlayList,userID,qd:QGridLayout):
        super().__init__()
        self.ID=id
        self.TenPlayList=TenPlayList
        self.userID=userID
        self.like =False
        self.qd=qd
        self.setupUi()

    def setupUi(self):
        self.resize(585, 94)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 10, 571, 80))
        self.frame.setStyleSheet("background-color: rgb(112, 66, 100);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lblHinh = QtWidgets.QLabel(parent=self.frame)
        self.lblHinh.setGeometry(QtCore.QRect(0, 10, 61, 61))
        self.lblHinh.setText("")        
        self.lblHinh.setObjectName("lblHinh")
        self.lblTenBaiHat = QtWidgets.QLabel(parent=self.frame)
        self.lblTenBaiHat.setGeometry(QtCore.QRect(70, 20, 111, 16))
        self.lblTenBaiHat.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblTenBaiHat.setObjectName("lblTenBaiHat")
        self.lblmaPlaylist = QtWidgets.QLabel(parent=self.frame)
        self.lblmaPlaylist.setGeometry(QtCore.QRect(70, 40, 111, 16))
        self.lblmaPlaylist.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblmaPlaylist.setObjectName("lblmaPlaylist")


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/icons8-play-button-circled-24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.btnPlayList = QtWidgets.QPushButton(parent=self.frame)
        self.btnPlayList.setGeometry(QtCore.QRect(390, 10, 51, 61))
        self.btnPlayList.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/icons8-playlist-30.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnPlayList.setIcon(icon1)
        self.btnPlayList.setIconSize(QtCore.QSize(50, 50))
        self.btnPlayList.setObjectName("btnPlayList")
        self.btnPlayList.clicked.connect(lambda:self.showMusiclst(self.qd))



        self.retranslateUi()

    def retranslateUi(self):
        self.lblTenBaiHat.setText("Tên Play List : "+str(self.TenPlayList))
        self.lblmaPlaylist.setText("Mã PlayList : "+str(self.ID))
        self.lblHinh.setScaledContents(True)

    def showMusiclst(self,f:QGridLayout):
        # Lấy dữ liệu và thêm các widget mới vào bố trí
        client = GetDataFromServer()
        client.connect()
        lstPlaylistDetail = client.sendSignal("GET_SONGS_OF_PLAYLIST_" + self.ID)
        lstMusic = client.sendSignal("GET_MUSIC_LIST")
        row = 0
   
        for playlistdetail in lstPlaylistDetail:
            musicID = int(playlistdetail["songid"])
            for music in lstMusic:
                if music["id"] == musicID:
                    self.baihat1 = baihat1.baihat1(str(music["id"]), str(music["name"]), str(music["artist"]), str(music["luotNghe"]), str(music["img"]), str(music["mp3"]), self.ID)
                    f.addWidget(self.baihat1,row,0)
                    row+=1 






 


if __name__ == "__main__":
    pl = Ui_Form()
