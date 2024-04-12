
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from Music import Music
import ImageResizer
import NhacBUS
import pygame
import os
from Category_BUS import Category_BUS
class Nhac_GUI(QWidget):
        def __init__(self):
                super().__init__()
                self.initUI()
        def initUI(self):
                self.resize(670, 550)
                self.content = QtWidgets.QFrame(self)
                self.content.setGeometry(QtCore.QRect(0, 0, 670, 550))
                self.content.setStyleSheet("background-color: #F6F6F6;\n"
        "")
                self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.content.setObjectName("content")
                self.scrollArea = QtWidgets.QScrollArea(parent=self.content)
                self.scrollArea.setGeometry(QtCore.QRect(20, 250, 630, 300))
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 628, 298))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                self.table = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents)
                self.table.setGeometry(QtCore.QRect(0, 0, 630, 300))
                self.table.setObjectName("table")
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.frame = QtWidgets.QFrame(parent=self.content)
                self.frame.setGeometry(QtCore.QRect(20, 20, 630, 210))
                self.frame.setStyleSheet("background-color:#FFE2E2 ;")
                self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame.setObjectName("frame")
                self.label = QtWidgets.QLabel(parent=self.frame)
                self.label.setGeometry(QtCore.QRect(20, 10, 31, 16))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(parent=self.frame)
                self.label_2.setGeometry(QtCore.QRect(20, 40, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(parent=self.frame)
                self.label_3.setGeometry(QtCore.QRect(20, 70, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(parent=self.frame)
                self.label_4.setGeometry(QtCore.QRect(20, 100, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(parent=self.frame)
                self.label_5.setGeometry(QtCore.QRect(20, 130, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(parent=self.frame)
                self.label_6.setGeometry(QtCore.QRect(20, 160, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_6.setFont(font)
                self.label_6.setObjectName("label_6")
                self.txtID = QtWidgets.QLineEdit(parent=self.frame)
                self.txtID.setGeometry(QtCore.QRect(130, 10, 150, 20))
                self.txtID.setStyleSheet("background-color: #FFFFFF;\n"
        "")
                self.txtID.setObjectName("txtID")
                self.txtName = QtWidgets.QLineEdit(parent=self.frame)
                self.txtName.setGeometry(QtCore.QRect(130, 70, 150, 20))
                self.txtName.setStyleSheet("background-color: #FFFFFF;\n"
        "")
                self.txtName.setObjectName("txtName")
                self.txtArtist = QtWidgets.QLineEdit(parent=self.frame)
                self.txtArtist.setGeometry(QtCore.QRect(130, 100, 150, 20))
                self.txtArtist.setStyleSheet("background-color: #FFFFFF;\n"
        "")
                self.txtArtist.setObjectName("txtArtist")
                self.txtimg = QtWidgets.QLineEdit(parent=self.frame)
                self.txtimg.setGeometry(QtCore.QRect(130, 130, 150, 20))
                self.txtimg.setStyleSheet("background-color: #FFFFFF;\n"
        "")
                self.txtimg.setObjectName("txtimg")
                self.txtmp3 = QtWidgets.QLineEdit(parent=self.frame)
                self.txtmp3.setGeometry(QtCore.QRect(130, 160, 150, 20))
                self.txtmp3.setStyleSheet("background-color: #FFFFFF;\n"
        "")
                self.txtmp3.setObjectName("txtmp3")
                self.cbCate = QtWidgets.QComboBox(parent=self.frame)
                self.cbCate.setGeometry(QtCore.QRect(130, 40, 151, 22))
                self.cbCate.setObjectName("cbCate")
                self.imgLB = QtWidgets.QLabel(parent=self.frame)
                self.imgLB.setGeometry(QtCore.QRect(300, 10, 101, 101))
                self.imgLB.setStyleSheet("background-color: #fff;")
                self.imgLB.setObjectName("imgLB")
                self.btnIMG = QtWidgets.QPushButton(parent=self.frame)
                self.btnIMG.setGeometry(QtCore.QRect(280, 130, 31, 20))
                self.btnIMG.setText("")
                
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("TienNuAdmin/img/photo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnIMG.setIcon(icon)
                self.btnIMG.setObjectName("btnIMG")
                self.btnMusic = QtWidgets.QPushButton(parent=self.frame)
                self.btnMusic.setGeometry(QtCore.QRect(280, 160, 31, 21))
                self.btnMusic.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("TienNuAdmin/img/music-notes.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnMusic.setIcon(icon1)
                self.btnMusic.setObjectName("btnMusic")
                
                self.btnPlay = QtWidgets.QPushButton(parent=self.frame)
                self.btnPlay.setGeometry(QtCore.QRect(20, 180, 31, 21))
                self.btnPlay.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("TienNuAdmin/img/play-button.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnPlay.setIcon(icon2)
                self.btnPlay.setObjectName("btnPlay")
                
                self.btnStop = QtWidgets.QPushButton(parent=self.frame)
                self.btnStop.setGeometry(QtCore.QRect(20, 180, 31, 21))
                self.btnStop.setText("")
                iconStop = QtGui.QIcon()
                iconStop.addPixmap(QtGui.QPixmap("TienNuAdmin/img/stop-button.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnStop.setIcon(iconStop)
                self.btnStop.setObjectName("btnStop")
                self.btnStop.setVisible(False)
                self.btnFind = QtWidgets.QPushButton(parent=self.frame)
                self.btnFind.setGeometry(QtCore.QRect(600, 40, 21, 21))
                self.btnFind.setText("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("TienNuAdmin/img/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnFind.setIcon(icon3)
                self.btnFind.setObjectName("btnFind")
                self.cbFind = QtWidgets.QComboBox(parent=self.frame)
                self.cbFind.setGeometry(QtCore.QRect(450, 10, 171, 22))
                self.cbFind.setObjectName("cbFind")
                self.txtFind = QtWidgets.QLineEdit(parent=self.frame)
                self.txtFind.setGeometry(QtCore.QRect(450, 40, 150, 20))
                self.txtFind.setStyleSheet("background-color: #FFFFFF;\n"
        "")
                self.txtFind.setObjectName("txtFind")
                self.addBtn = QtWidgets.QPushButton(parent=self.frame)
                self.addBtn.setGeometry(QtCore.QRect(450, 70, 171, 25))
                self.addBtn.setStyleSheet("background-color: #ECB159;")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("TienNuAdmin/img/plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.addBtn.setIcon(icon4)
                self.addBtn.setObjectName("addBtn")
                self.updateBtn = QtWidgets.QPushButton(parent=self.frame)
                self.updateBtn.setGeometry(QtCore.QRect(450, 100, 171, 25))
                self.updateBtn.setStyleSheet("background-color: #ECB159;")
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("TienNuAdmin/img/system-update.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.updateBtn.setIcon(icon5)
                self.updateBtn.setObjectName("updateBtn")
                self.deleteBtn = QtWidgets.QPushButton(parent=self.frame)
                self.deleteBtn.setGeometry(QtCore.QRect(450, 130, 171, 25))
                self.deleteBtn.setStyleSheet("background-color: #ECB159;")
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap("TienNuAdmin/img/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.deleteBtn.setIcon(icon6)
                self.deleteBtn.setObjectName("deleteBtn")
                self.refreshBtn = QtWidgets.QPushButton(parent=self.frame)
                self.refreshBtn.setGeometry(QtCore.QRect(450, 160, 171, 25))
                self.refreshBtn.setStyleSheet("background-color: #ECB159;")
                icon7 = QtGui.QIcon()
                icon7.addPixmap(QtGui.QPixmap("TienNuAdmin/img/loading-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.refreshBtn.setIcon(icon7)
                self.refreshBtn.setObjectName("refreshBtn")
                #-----------------Dat item cho combobox
                self.cbFind.addItem("ID")
                self.cbFind.addItem("Songs name")
                self.cbFind.addItem("Artist")
                self.cbFind.addItem("Category")
                
                #-------------------------------------------------
                #Dat lenh cho button
                self.btnIMG.clicked.connect(self.chooseIMG)
                self.retranslateUi()
                
                self.btnFind.clicked.connect(self.searchData)
                
                self.txtFind.returnPressed.connect(self.searchData)
                self.btnPlay.clicked.connect(self.playSong)
                self.btnStop.clicked.connect(self.stopPlaySong)
                self.btnMusic.clicked.connect(self.chooseSongFile)
                #----------Khoa textline
                self.txtimg.setReadOnly(True)
                self.txtmp3.setReadOnly(True)
                
                #---------------------------------------
                musicBus = NhacBUS.NhacBUS()
                
                self.addDataToTable(musicBus.getData())
                self.table.itemClicked.connect(self.setDataClicked)
                
                self.addBtn.clicked.connect(self.addSong)
                self.refreshBtn.clicked.connect(lambda:self.addDataToTable(musicBus.getData()))
        
        def retranslateUi(self):
                self.label.setText( "ID :")
                self.label_2.setText("CATEGORY:")
                self.label_3.setText("NAME: ")
                self.label_4.setText( "ARTIST: ")
                self.label_5.setText( "IMG SOURCE: ")
                self.label_6.setText( "MP3 SOURCE: ")
                self.imgLB.setText( "imgHere")
                self.addBtn.setText( "ADD")
                self.updateBtn.setText("UPDATE")
                self.deleteBtn.setText( "DELETE")
                self.refreshBtn.setText( "REFRESH")
        def addDataToTable(self, lstMusic:list):
                self.table.clearContents()
                self.table.setRowCount(0)
                self.table.setColumnCount(0)
                #Reset lai cb truong hop co du lieu category moi
                self.setCBItems()
                
                self.table.setColumnCount(6)
                lstHead = ['ID', 'CategoryID', 'Name', 'Artist', 'Imgsource','MP3_source']
                self.table.setHorizontalHeaderLabels(lstHead)
               
                #bus = NhacBUS.NhacBUS()
                row_count = len(lstMusic);
                self.table.setRowCount(row_count)
                row = 0;
                for music in  lstMusic:
                        self.table.setItem(row, 0,QTableWidgetItem(str(music.id)))
                        self.table.setItem(row, 1,QTableWidgetItem(str(music.catID)))
                        self.table.setItem(row, 2,QTableWidgetItem(str(music.name)))
                        self.table.setItem(row, 3,QTableWidgetItem(str(music.artist)))
                        self.table.setItem(row, 4,QTableWidgetItem(str(music.img)))
                        self.table.setItem(row, 5,QTableWidgetItem(str(music.mp3)))
                        row += 1
                
        def setCBItems(self):
                catBus = Category_BUS()
                lstItems = []
                for cat in catBus.getData():
                        lstItems.append(cat.title)
                
                self.cbCate.addItems(lstItems)
        def setDataClicked(self,item):
                row = item.row()
                self.btnStop.setVisible(False)
                self.txtID.setText(self.table.item(row,0).text())
                self.txtName.setText(self.table.item(row,2).text())
                self.txtArtist.setText(self.table.item(row,3).text())
                self.cbCate.setCurrentIndex(int(self.table.item(row,1).text())-1)
                self.txtimg.setText(self.table.item(row,4).text())
                self.txtmp3.setText(self.table.item(row,5).text())
                img = self.txtimg.text()
                pixmap = QPixmap()
                pixmap.loadFromData(ImageResizer.resizeImg(img,101,101))
                self.imgLB.setPixmap(pixmap)
        def chooseIMG(self):
                file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
                
                if file_path:
                # Check if the file is located in the SongIMG folder
                        folder_path = os.path.dirname(file_path)
                        if folder_path.endswith("SongIMG"):
                # Check if the selected file is an image file
                                _, file_extension = os.path.splitext(file_path)
                                if file_extension.lower() in ('.jpg', '.jpeg', '.png', '.gif', '.bmp','.jfif'):
                    # Set selected file path to QLineEdit
                                        self.txtimg.setText(os.path.basename(file_path))
                                        img = self.txtimg.text()
                                        pixmap = QPixmap()
                                        pixmap.loadFromData(ImageResizer.resizeImg(img,101,101))
                                        self.imgLB.setPixmap(pixmap)
                                else:
                    # Show message box alert for non-image file
                                        QMessageBox.warning(self, "Warning", "Please select an image file.", QMessageBox.StandardButton.Ok)
                        else:
                # Show message box alert for file outside SongIMG folder
                                QMessageBox.warning(self, "Warning", "Please select a file from the SongIMG folder.", QMessageBox.StandardButton.Ok)
        def searchData(self):
                item = self.cbFind.currentIndex()
                data = self.txtFind.text()
                lstFound = []
                nhacbus = NhacBUS.NhacBUS()
                if item == 0: #Tim theo id
                        lstFound = nhacbus.findSongByID(data)
                elif item == 3:#Tim theo the loai
                        lstFound = nhacbus.findSongByCategoryID(data)
                elif item == 1:#Tim theo ten nhac
                        lstFound = nhacbus.findSongByName(data)
                else:#Tim theo ten tac gia
                        lstFound = nhacbus.findSongByArtist(data)
                self.addDataToTable(lstFound)
        def playSong(self):
                self.btnStop.setVisible(True)
                pygame.mixer.init()

                songPath = "TienNuAdmin/song/"+ self.txtmp3.text()
                pygame.mixer.stop()
                try:
            # Load the song using pygame mixer
                        song = pygame.mixer.Sound(songPath)
                        song.play()
                except Exception as e:
                        QMessageBox.information(None, "Thông báo!", "Lỗi khi phát nhạc!")
                        self.btnStop.setVisible(False)
        def stopPlaySong(self):
                self.btnStop.setVisible(False)
                pygame.mixer.stop()
        def chooseSongFile(self):
                file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
                
                if file_path:
                # Check if the file is located in the SongIMG folder
                        folder_path = os.path.dirname(file_path)
                        if folder_path.endswith("song"):
                # Check if the selected file is an image file
                                _, file_extension = os.path.splitext(file_path)
                                if file_extension.lower() in ('.mp3', '.wav'):
                    # Set selected file path to QLineEdit
                                        self.txtmp3.setText(os.path.basename(file_path))
                                else:
                    # Show message box alert for non-image file
                                        QMessageBox.warning(self, "Warning", "Please select an MP3 or WAV file.", QMessageBox.StandardButton.Ok)
                        else:
                # Show message box alert for file outside SongIMG folder
                                QMessageBox.warning(self, "Warning", "Please select a file from the song folder.", QMessageBox.StandardButton.Ok)             
        def addSong(self):
                bus= NhacBUS.NhacBUS()
                song = Music(None,self.cbCate.currentIndex()+1,self.txtName.text(),self.txtArtist.text(),self.txtimg.text(),self.txtmp3.text(),0)
                
                bus.addSong(song)
                self.addDataToTable(bus.getData())
                

