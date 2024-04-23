# Form implementation generated from reading ui file 'baihat.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import pygame
from GetDataFromServer import GetDataFromServer



class baihat1(QWidget):
    def __init__(self,id,TenBaiHat,TacGia,ThoiLuong,TenHinh,mp3,userID):
        super().__init__()
        self.ID=id
        self.TenBaiHat=TenBaiHat
        self.TacGia=TacGia
        self.ThoiLuong=ThoiLuong
        self.TenHinh=TenHinh
        self.mp3=mp3
        self.userID=userID
        self.like =False
        self.setUi()
    def setUi(self):
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
        self.lblTacGia = QtWidgets.QLabel(parent=self.frame)
        self.lblTacGia.setGeometry(QtCore.QRect(70, 40, 111, 16))
        self.lblTacGia.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblTacGia.setObjectName("lblTacGia")
        self.lblThoiLuong = QtWidgets.QLabel(parent=self.frame)
        self.lblThoiLuong.setGeometry(QtCore.QRect(200, 30, 31, 16))
        self.lblThoiLuong.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblThoiLuong.setObjectName("lblThoiLuong")
        self.btnPlay = QtWidgets.QPushButton(parent=self.frame)
        self.btnPlay.setGeometry(QtCore.QRect(310, 10, 51, 61))
        self.btnPlay.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("TienNuClient/imgs/icons8-play-button-circled-24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnPlay.setIcon(icon)
        self.btnPlay.setIconSize(QtCore.QSize(50, 50))
        self.btnPlay.setObjectName("btnPlay")
        self.btnPlay.clicked.connect(self.playSong)
        
        self.btnPlayList = QtWidgets.QPushButton(parent=self.frame)
        self.btnPlayList.setGeometry(QtCore.QRect(390, 10, 51, 61))
        self.btnPlayList.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("TienNuClient/imgs/icons8-playlist-30.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnPlayList.setIcon(icon1)
        self.btnPlayList.setIconSize(QtCore.QSize(50, 50))
        self.btnPlayList.setObjectName("btnPlayList")
        self.btnPlayList.clicked.connect(self.sendRemovePlaylist)
        self.btnLike = QtWidgets.QPushButton(parent=self.frame)
        self.btnLike.setGeometry(QtCore.QRect(460, 10, 51, 61))
        self.btnLike.setText("")
        client = GetDataFromServer()
        client.connect()
        lstMS = client.sendSignal("GET_FAVORITE_LIST_" + self.userID)
        for lst in lstMS:
            if int(self.ID) == lst["songID"]:
                self.like=True
        if self.like :
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("TienNuClient/imgs/heart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btnLike.setIcon(icon2)            
        else :         
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("TienNuClient/imgs/icons8-favorite-24 (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btnLike.setIcon(icon2)
        self.btnLike.clicked.connect(self.toggleFavorite)
        self.btnLike.setIconSize(QtCore.QSize(50, 50))
        self.btnLike.setObjectName("btnLike")
       
        self.retranslateUi()

    def retranslateUi(self):
        self.lblTenBaiHat.setText("Tên Bài Hát : "+str(self.TenBaiHat))
        self.lblTacGia.setText("Tác Giả : "+str(self.TacGia))   
        self.lblThoiLuong.setText("Lượt Nghe : "+str(self.ThoiLuong))
        self.lblHinh.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("TienNuClient/imgs/" + self.TenHinh)))
        self.lblHinh.setScaledContents(True)

    def playSong(self):
                # self.btnStop.setVisible(True)
                g = GetDataFromServer()
                g.connect()
                pygame.mixer.init()
                try:
            # # Load the song using pygame mixer
                        g.playSongFromServer(self.ID)
                except Exception as e:
                        QMessageBox.information(None, "Thông báo!", "Lỗi khi phát nhạc!")
                        # self.btnStop.setVisible(False)
    def stopPlaySong(self):
                # self.btnStop.setVisible(False)
                pygame.mixer.stop()
                self.btnPlay.clicked.connect(self.playSong)
    def sendAddToFavorite(self):
        client = GetDataFromServer()
        client.connect()
        receive = client.sendAddToPlaylist("ADD_TO_FAVORITE_" + self.userID + "_" + self.ID)
        print(receive)
    def sendRemovePlaylist(self):
        client = GetDataFromServer()
        client.connect()
        receive = client.sendRemovePlayList("REMOVE_TO_PLAYLIST_" + self.userID + "_" + self.ID)
        print(receive)
    def sendRemoveToFavorite(self):
        client = GetDataFromServer()
        client.connect()
        receive = client.sendRemoveFavorite("REMOVE_TO_FAVORITE_" + self.userID + "_" + self.ID)
        print(receive)
    def toggleFavorite(self):
        # Kiểm tra trạng thái hiện tại của nút yêu thích
        if self.like:
            # Nếu đã thích, gửi yêu cầu xóa khỏi danh sách yêu thích
            self.sendRemoveToFavorite()
            # Đổi trạng thái yêu thích về False
            self.like = False
            # Thay đổi biểu tượng của nút yêu thích
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("TienNuClient/imgs/icons8-favorite-24 (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btnLike.setIcon(icon2)
        else:
            # Nếu chưa thích, gửi yêu cầu thêm vào danh sách yêu thích
            self.sendAddToFavorite()
            # Đổi trạng thái yêu thích về True
            self.like = True
            # Thay đổi biểu tượng của nút yêu thích
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("TienNuClient/imgs/heart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btnLike.setIcon(icon2)       

if __name__ == "__main__":
    bh=baihat1()

