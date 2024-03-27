
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from Slide import Slide,SlideDetail
from SlideBUS import *
from NhacBUS import NhacBUS
class SlideGUI(QWidget):
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
                self.scrollArea.setGeometry(QtCore.QRect(20, 250, 251, 300))
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 298))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                self.tableSlide = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents)
                self.tableSlide.setGeometry(QtCore.QRect(0, 0, 250, 311))
                self.tableSlide.setObjectName("tableSlide")
                self.tableSlide.setColumnCount(0)
                self.tableSlide.setRowCount(0)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.frame = QtWidgets.QFrame(parent=self.content)
                self.frame.setGeometry(QtCore.QRect(20, 20, 630, 210))
                self.frame.setStyleSheet("background-color:#FFE2E2 ;")
                self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame.setObjectName("frame")
                self.label = QtWidgets.QLabel(parent=self.frame)
                self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.label_3 = QtWidgets.QLabel(parent=self.frame)
                self.label_3.setGeometry(QtCore.QRect(20, 40, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.txtid = QtWidgets.QLineEdit(parent=self.frame)
                self.txtid.setGeometry(QtCore.QRect(130, 10, 150, 20))
                self.txtid.setStyleSheet("background-color: #FFFFFF;\n"
        "")
                self.txtid.setObjectName("txtid")
                self.txttitle = QtWidgets.QLineEdit(parent=self.frame)
                self.txttitle.setGeometry(QtCore.QRect(130, 40, 150, 20))
                self.txttitle.setStyleSheet("background-color: #FFFFFF;\n"
        "")
                self.txttitle.setObjectName("txttitle")
                self.btnFind = QtWidgets.QPushButton(parent=self.frame)
                self.btnFind.setGeometry(QtCore.QRect(600, 40, 21, 21))
                self.btnFind.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("TienNuAdmin/img/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnFind.setIcon(icon)
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
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("TienNuAdmin/img/plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.addBtn.setIcon(icon1)
                self.addBtn.setObjectName("addBtn")
                self.refreshBtn = QtWidgets.QPushButton(parent=self.frame)
                self.refreshBtn.setGeometry(QtCore.QRect(450, 160, 171, 25))
                self.refreshBtn.setStyleSheet("background-color: #ECB159;")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("TienNuAdmin/img/loading-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.refreshBtn.setIcon(icon2)
                self.refreshBtn.setObjectName("refreshBtn")
                self.btnupdate = QtWidgets.QPushButton(parent=self.frame)
                self.btnupdate.setGeometry(QtCore.QRect(450, 100, 171, 25))
                self.btnupdate.setStyleSheet("background-color: #ECB159;")
                icon3= QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("TienNuAdmin/img/system-update.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnupdate.setIcon(icon3)
                self.btnupdate.setObjectName("btnupdate")
                self.btndelete = QtWidgets.QPushButton(parent=self.frame)
                self.btndelete.setGeometry(QtCore.QRect(450, 130, 171, 25))
                self.btndelete.setStyleSheet("background-color: #ECB159;")
                icon4= QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("TienNuAdmin/img/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btndelete.setIcon(icon4)
                self.btndelete.setObjectName("btndelete")
                self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.content)
                self.scrollArea_2.setGeometry(QtCore.QRect(290, 250, 361, 301))
                self.scrollArea_2.setWidgetResizable(True)
                self.scrollArea_2.setObjectName("scrollArea_2")
                self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
                self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 359, 299))
                self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
                self.tableDetail = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents_2)
                self.tableDetail.setGeometry(QtCore.QRect(0, 0, 360, 300))
                self.tableDetail.setObjectName("tableDetail")
                self.tableDetail.setColumnCount(0)
                self.tableDetail.setRowCount(0)
                self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
                self.retranslateUi()
                
                slideBUS = SlideBUS()
                self.addDataToTableSlide(slideBUS.getData())
                self.tableSlide.itemClicked.connect(self.setDataClicked)
        def retranslateUi(self):
                self.label.setText(( "SLIDE ID:"))
                self.label_3.setText(( "SLIDE TITLE:"))
                self.addBtn.setText(( "ADD"))
                self.refreshBtn.setText(( "REFRESH"))
                self.btnupdate.setText(( "UPDATE"))
                self.btndelete.setText(( "DELETE"))
        def addDataToTableSlide(self, lstSlide:list):
                self.tableSlide.setColumnCount(2)
                lstHead = ["SlideID", "SlideTitle"]
                rowCount = len(lstSlide)
                self.tableSlide.setRowCount(rowCount)
                self.tableSlide.setHorizontalHeaderLabels(lstHead)
                row = 0
                for slide in lstSlide:
                        self.tableSlide.setItem(row,0,QTableWidgetItem(str(slide.slideid)))
                        self.tableSlide.setItem(row,1,QTableWidgetItem(str(slide.slideTitle)))
                        row +=1
        def setDataClicked(self,item):
                row = item.row()
                slideid = int(self.tableSlide.item(row,0).text())
                slideDetailBUS = SlideDetailBUS()
                
                self.addDataToTableDetail(slideDetailBUS.getData(slideid))
        def addDataToTableDetail(self,lstDetail:list):
                self.tableDetail.setColumnCount(3)
                lstHead = ["SlideID", "SongID","Song name"]
                rowCount = len(lstDetail)
                self.tableDetail.setRowCount(rowCount)
                self.tableDetail.setHorizontalHeaderLabels(lstHead)
                musicBUS = NhacBUS()
                row = 0
                for detail in lstDetail:
                        self.tableDetail.setItem(row,0,QTableWidgetItem(str(detail.slideid)))
                        self.tableDetail.setItem(row,1,QTableWidgetItem(str(detail.songid)))
                        song = musicBUS.getMusicByID(detail.songid)
                        self.tableDetail.setItem(row,2,QTableWidgetItem(str(song.name)))
                        row +=1
                        

                
                          
                
                
