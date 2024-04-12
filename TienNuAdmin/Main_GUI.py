# Form implementation generated from reading ui file 'Main_GUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys
import Category_GUI
import UserGUI
from ServerGUI import ServerGUI
import Nhac_GUI
import SlideGUI
class Main_GUI(QMainWindow):
        def __init__(self):
                super().__init__()
                self.initUI();
                
        def initUI(self):
                self.resize(800, 600)
                self.centralwidget = QWidget()
                self.centralwidget.setObjectName("centralwidget")
                self.content = QFrame(parent=self.centralwidget)
                self.content.setGeometry(QtCore.QRect(-1, -1, 800, 600))
                self.content.setStyleSheet("background-color: #F6F6F6;")
                self.content.setFrameShape(QFrame.Shape.StyledPanel)
                self.content.setFrameShadow(QFrame.Shadow.Raised)
                self.content.setObjectName("content")
                self.leftMenuPn = QFrame(parent=self.content)
                self.leftMenuPn.setGeometry(QtCore.QRect(0, 0, 130, 600))
                self.leftMenuPn.setStyleSheet("background-color: #FFC7C7;")
                self.leftMenuPn.setFrameShape(QFrame.Shape.StyledPanel)
                self.leftMenuPn.setFrameShadow(QFrame.Shadow.Raised)
                self.leftMenuPn.setObjectName("leftMenuPn")
                self.icon = QLabel(parent=self.leftMenuPn)
                self.icon.setGeometry(QtCore.QRect(0, 0, 130, 130))
                self.icon.setText("")
                self.icon.setPixmap(QtGui.QPixmap("TienNuAdmin\img\icon.png"))
                self.icon.setObjectName("icon")
                self.btnMusic = QPushButton(parent=self.leftMenuPn)
                self.btnMusic.setGeometry(QtCore.QRect(10, 170, 110, 30))
                self.btnMusic.setStyleSheet("background-color: #8785A2;\n"
        "color: #F6F6F6;")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("TienNuAdmin\img/music.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnMusic.setIcon(icon)
                self.btnMusic.setObjectName("btnMusic")
                self.btnCategory = QPushButton(parent=self.leftMenuPn)
                self.btnCategory.setGeometry(QtCore.QRect(10, 220, 110, 30))
                self.btnCategory.setStyleSheet("background-color: #8785A2;\n"
        "color: #F6F6F6;")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("TienNuAdmin\img/options.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnCategory.setIcon(icon1)
                self.btnCategory.setObjectName("btnCategory")
                self.btnUser = QPushButton(parent=self.leftMenuPn)
                self.btnUser.setGeometry(QtCore.QRect(10, 270, 110, 30))
                self.btnUser.setStyleSheet("background-color: #8785A2;\n"
        "color: #F6F6F6;")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("TienNuAdmin\img/teamwork.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnUser.setIcon(icon2)
                self.btnUser.setObjectName("btnUser")
        #         self.btnslide = QPushButton(parent=self.leftMenuPn)
        #         self.btnslide.setGeometry(QtCore.QRect(10, 320, 110, 30))
        #         self.btnslide.setStyleSheet("background-color: #8785A2;\n"
        # "color: #F6F6F6;")
        #         icon3 = QtGui.QIcon()
        #         icon3.addPixmap(QtGui.QPixmap("TienNuAdmin\img/slider.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        #         self.btnslide.setIcon(icon3)
        #         self.btnslide.setObjectName("btnslide")
                self.btnServer = QPushButton(parent=self.leftMenuPn)
                self.btnServer.setGeometry(QtCore.QRect(10, 370, 110, 30))
                self.btnServer.setStyleSheet("background-color: #8785A2;\n"
        "color: #F6F6F6;")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("TienNuAdmin\img/server.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnServer.setIcon(icon4)
                self.btnServer.setObjectName("btnServer")
                self.titlePn = QFrame(parent=self.content)
                self.titlePn.setGeometry(QtCore.QRect(130, 0, 670, 50))
                self.titlePn.setStyleSheet("background-color: #8785A2;\n"
        "")
                self.titlePn.setFrameShape(QFrame.Shape.StyledPanel)
                self.titlePn.setFrameShadow(QFrame.Shadow.Raised)
                self.titlePn.setObjectName("titlePn")
                self.pageTitleLB = QLabel(parent=self.titlePn)
                self.pageTitleLB.setGeometry(QtCore.QRect(0, 0, 670, 50))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.pageTitleLB.setFont(font)
                self.pageTitleLB.setStyleSheet("color: #F6F6F6;")
                self.pageTitleLB.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.pageTitleLB.setObjectName("pageTitleLB")
                
                #-------------------------Trang
                self.pagesPn = QFrame(parent=self.content)
                self.pagesPn.setGeometry(QtCore.QRect(130, 50, 670, 550))
                self.pagesPn.setStyleSheet("background-color: #F6F6F6;\n"
        "")
                self.pagesPn.setFrameShape(QFrame.Shape.StyledPanel)
                self.pagesPn.setFrameShadow(QFrame.Shadow.Raised)
                self.pagesPn.setObjectName("pagesPn")
                self.pagesWidget = QStackedWidget(parent=self.pagesPn)
                self.pagesWidget.setGeometry(QtCore.QRect(0, 0, 670, 550))
                self.pagesWidget.setObjectName("pagesWidget")
                self.musicGUI = Nhac_GUI.Nhac_GUI()
                self.musicGUI.setObjectName("musicGUI")
                self.pagesWidget.addWidget(self.musicGUI)
                self.catGUI = Category_GUI.Category_GUI()
                self.catGUI.setObjectName("catGUI")
                self.pagesWidget.addWidget(self.catGUI)
                self.usergui = UserGUI.UserGUI()
                self.usergui.setObjectName("usergui")
                self.pagesWidget.addWidget(self.usergui)
                # self.slideGUI = SlideGUI.SlideGUI()
                # self.slideGUI.setObjectName("slideGUI")
                # self.pagesWidget.addWidget(self.slideGUI)
                self.serverGUI = ServerGUI()
                self.serverGUI.setObjectName("serverGUI")
                self.pagesWidget.addWidget(self.serverGUI)
                self.setCentralWidget(self.centralwidget)
                #----------------------------gan link cho btn
                self.btnMusic.clicked.connect(self.toMusic)
                self.btnCategory.clicked.connect(self.toCat)
                self.btnUser.clicked.connect(self.toUser)
                # self.btnslide.clicked.connect(self.toSlide)
                self.btnServer.clicked.connect(self.toServer)
                #--------------------------------------------

                self.retranslateUi()
                self.pagesWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(self)

        def retranslateUi(self):
                self.btnMusic.setText( "Music")
                self.btnCategory.setText("Categories")
                self.btnUser.setText( "Users")
                # self.btnslide.setText( "Slides")
                self.btnServer.setText( "Server")
                self.pageTitleLB.setText( "MUSICS MANAGEMENT")
        def toMusic(self):
                self.pageTitleLB.setText("MUSICS MANAGEMENT")
                self.pagesWidget.setCurrentWidget(self.musicGUI)
        def toCat(self):
                self.pageTitleLB.setText("CATEGORIES MANAGEMENT")
                self.pagesWidget.setCurrentWidget(self.catGUI)
        def toUser(self):
                self.pageTitleLB.setText("USERS MANAGEMENT")
                self.pagesWidget.setCurrentWidget(self.usergui)
        # def toSlide(self):
        #         self.pageTitleLB.setText("SLIDE MANAGEMENT")
        #         self.pagesWidget.setCurrentWidget(self.slideGUI)
        def toServer(self):
                self.pageTitleLB.setText("SERVER MANAGEMENT")
                self.pagesWidget.setCurrentWidget(self.serverGUI)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Main_GUI()
    ui.show()
    sys.exit(app.exec())


