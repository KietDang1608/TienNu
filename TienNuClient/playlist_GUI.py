# Form implementation generated from reading ui file 'playlist_GUI.ui'
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
import playlists
from GetDataFromServer import GetDataFromServer
class playlist_GUI(QWidget):
    def __init__(self,userIDDemo):
        super().__init__()
        self.userIDDemo=userIDDemo
        print(userIDDemo)
        self.setUi()
    def setUi(self):
        self.setObjectName("Form")
        self.resize(611, 591)
        # self.addDataToWidget(playlist_BUS.getData())


        self.scrollArea = QtWidgets.QScrollArea(parent=self)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 611, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 589))
        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.scrollAreaWidgetContents.setLayout(self.layout)
        self.getPlaylistID()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.btnAddPlaylist = QtWidgets.QPushButton(parent=self)
        self.btnAddPlaylist.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.btnAddPlaylist.setObjectName("btnAddPlaylist")
        self.btnAddPlaylist.setText("Add Playlist")
        self.btnAddPlaylist.setStyleSheet("background-color: #70bf73; color: white;")
        self.btnAddPlaylist.clicked.connect(self.addPlayList)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))

    def getPlaylistID(self):
        userIDDemoa = str(self.userIDDemo)  # Example user ID
        client = GetDataFromServer()
        client.connect()
        # lstMusic_playlist = client.sendSignal("GET_PLAYLIST_LIST_" + self.userIDDemo)
        lst = client.sendSignal("GET_PLAYLIST_LIST_" + self.userIDDemo)
        # print(lstMusic_playlist)
    
       
        # row=0
        # for playlist in lstMusic_playlist:
        #     playlistID=str(playlist["id"])
            
        #     lstPlaylistDetail = client.sendSignal("GET_SONGS_OF_PLAYLIST_" + playlistID)
        #     lstMusic = client.sendSignal("GET_MUSIC_LIST")
        #     for playlistdetail in lstPlaylistDetail:
        #         musicID=int(playlistdetail["songid"])
        #         for music in lstMusic:
        #             if music["id"] == musicID:
        #                  self.baihat=baihat.baihat(str(music["id"]),str(music["name"]),str(music["artist"]),str(music["luotNghe"]),str(music["img"]),str(music["mp3"]),self.userIDDemo)
        #                  self.layout.addWidget(self.baihat,row,0)
        #                  row+=1   
        row =0
        for pl in lst:
            self.playlists = playlists.Ui_Form(str(pl["id"]),str(pl["title"]),str(pl["userID"]),self.layout)
            self.layout.addWidget(self.playlists,row,0)
            row+=1 
    def addPlayList(self):
        dialog = QDialog()
        dialog.setWindowTitle("Thêm PlayList")
        dialog.setFixedSize(300, 150)  

        layout = QVBoxLayout(dialog)


        label2 = QLabel("Tên PlayList: ")
        layout.addWidget(label2)
        lineEdit2 = QLineEdit()
        layout.addWidget(lineEdit2)

        # Thêm nút
        button = QPushButton("Thêm")
        button.clicked.connect(lambda: self.addPlaylistConfirmed(lineEdit2.text(),dialog))
        layout.addWidget(button)

        dialog.exec()
     

    def addPlaylistConfirmed(self, tenPlaylist,dialog):
        client = GetDataFromServer()
        client.connect()
        lst = client.sendSignal("ADD_PLAYLIST_" +self.userIDDemo + "_" +tenPlaylist)
        dialog.close()
        


    # def addDataToWidget(self, lstPlaylist:list):
    #     row=0
    #     for music in lstPlaylist:
    #         self.baihat=baihat.baihat(str(music.name),str(music.artist),str(music.luotNghe),str(music.img),str(music.mp3))
    #         self.layout.addWidget(self.baihat,row,0)
    #         row+=1
if __name__ == "__main__":
    pl=playlist_GUI()
