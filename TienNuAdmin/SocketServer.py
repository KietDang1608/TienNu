from Category_BUS import Category_BUS
from NhacBUS import NhacBUS
from FavoriteBUS import FavoriteBUS
from PlaylistBUS import PlaylistBUS,PlayListDetailBUS
from PyQt6.QtCore import QThread,pyqtSignal
from UserBUS import UserBUS
import pygame
import socket
import json
import os
class SocketServer(QThread):
    message_received = pyqtSignal(str)
    stopped =pyqtSignal()
    ip = 'localhost'#My LAN: 172.20.10.5
    port = 3306
    def __init__(self):
        super().__init__()
        self.running = False
        self.host = SocketServer.ip
        self.port = SocketServer.port
        self.serverSocket = None
        self.clientSocket = None
        self.clientAddress = None
        
        self.message = ""
    def run(self):
        self.running = True
        try:
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSocket.bind((self.host, self.port))
            self.serverSocket.listen(1)
            print(f"Server is listening on {self.host}: {self.port}")
            self.message = f"Server is listening on {self.host}: {self.port}"
            while True:
                self.getSignal()
                
        except Exception as e:
            print (f'Error starting server: {e}')
        self.stopped.emit()
    def stop(self):
        self.running = False
        try:
            if self.clientSocket:
                self.clientSocket.close();
            if self.serverSocket:
                self.serverSocket.close()
            print("Server stopped")
        except Exception as e:
            print(f"Error stopping server: {e}")
    
    def sendCategoryLIST(self):
        categoryBUS = Category_BUS()
        datadict = [vars(obj) for obj in categoryBUS.getData()]
        jsonData = json.dumps(datadict)
        self.clientSocket.sendall(jsonData.encode())
    def sendUserLIST(self):
        userBUS = UserBUS()
        users = userBUS.readData()
        for user in users:
            user.datecreate = str(user.datecreate)
        datadict = [vars(obj) for obj in users]
        jsonData = json.dumps(datadict)
        self.clientSocket.sendall(jsonData.encode())
    def sendMusicLIST(self):
        musicBUS = NhacBUS()
        datadict = [vars(obj) for obj in musicBUS.getData()]
        jsonData = json.dumps(datadict)
        self.clientSocket.sendall(jsonData.encode())
    def sendFavoriteLIST(self,userID):
        favBUS = FavoriteBUS()
        datadict = [vars(obj) for obj in favBUS.getFavSongsOfUser(userID)]
        jsonData = json.dumps(datadict)
        self.clientSocket.sendall(jsonData.encode())
    def sendPlaylistLIST(self,userID):
        playlistBUS = PlaylistBUS()
        datadict1 = [vars(obj) for obj in playlistBUS.getPLaylistByUserID(userID)]
        jsonData = json.dumps(datadict1)
        self.clientSocket.sendall(jsonData.encode())
    def sendSongsInPlaylist(self,playListID):
        detailBUS = PlayListDetailBUS()
        datadict = [vars(obj) for obj in detailBUS.getPlayListByID(playListID)]
        jsonData = json.dumps(datadict)
        self.clientSocket.sendall(jsonData.encode())
    def sendMusic(self,songID):
        nhacBUS = NhacBUS()
        mp3 = nhacBUS.getMP3FileByID(songID)
        filePath = "TienNuAdmin/song/" +mp3
        absolutePath = os.path.abspath(filePath)
        print(absolutePath)
        with open(absolutePath, "rb") as music_file:
            data = music_file.read(1024)
            while data:
                self.clientSocket.sendall(data)
                data = music_file.read(1024)
    def addToFAV(self,userid:str,songid:str):
        favBUS = FavoriteBUS()
        for fav in favBUS.getFavSongsOfUser(userid):
            if songid == str(fav.songID):
                self.clientSocket.sendall("0".encode())
                return 
        favBUS.addData(userid,songid)
        self.clientSocket.sendall("1".encode())

    def removeToFAV(self,userid:str,songid:str):
        favBUS = FavoriteBUS()
        for fav in favBUS.getFavSongsOfUser(userid):
            if songid == str(fav.songID):
                favBUS.delData(userid,songid)
                self.clientSocket.sendall("1".encode())
                return 
        self.clientSocket.sendall("0".encode())

    def addPlayList(self,id:str,songid:str):
        PlDetailBus = PlayListDetailBUS()  
        for pl in PlDetailBus.getPlayListByID(id):
            if songid == str(pl.songid):
                self.clientSocket.sendall("0".encode())
                return
        PlDetailBus.addData(id,songid)
        self.clientSocket.sendall("1".encode())

    def removePlayList(self,id:str,songid:str):
        PlDetailBus = PlayListDetailBUS()  
        for pl in PlDetailBus.getPlayListByID(id):
            if songid == str(pl.songid):
                PlDetailBus.delData(id,songid)
                self.clientSocket.sendall("1".encode())
                return
        self.clientSocket.sendall("0".encode())
    def addNewPlayList(self,id:str,userID,title:str):
        pl = PlaylistBUS()
        for fav in pl.getData():
            if id == str(fav.id):
                self.clientSocket.sendall("0".encode())
                return 
        pl.addData(id,userID,title)
        self.clientSocket.sendall("1".encode())

    def updateUser(self,username:str,name:str,password:str):
        userBUS = UserBUS()  
    
        userBUS.updateUser(password,name,username)
        self.clientSocket.sendall("1".encode())
        return
        

    # Hàm nhận tín hiệu gửi từ client, xem tín hiệu là gì tùy trường hợp mà gửi lại dữ liệu tương ứng
    def getSignal(self):
        self.clientSocket, self.clientAddress = self.serverSocket.accept()
        print(f"Connection established with {self.clientAddress}")
        signal = self.clientSocket.recv(1024).decode("utf-8")
        self.message = self.clientAddress.__str__() + ": " + signal
        
        print( "Tin hieu tu client: ",signal)
        if (signal == "GET_CATEGORY_LIST"):
            self.sendCategoryLIST()
        elif signal == "GET_MUSIC_LIST":
            self.sendMusicLIST()
        elif "GET_FAVORITE_LIST" in signal:
            userid = signal.replace("GET_FAVORITE_LIST_","")
            self.sendFavoriteLIST(userid)
        elif "GET_PLAYLIST_LIST" in signal:
            userid = signal.replace("GET_PLAYLIST_LIST_","")
            self.sendPlaylistLIST(userid)
        elif "GET_SONGS_OF_PLAYLIST" in signal:
            playlistid = signal.replace("GET_SONGS_OF_PLAYLIST_","")
            self.sendSongsInPlaylist(playlistid)
        elif "PLAY_SONG" in signal:
            songid = signal.replace("PLAY_SONG_","")
            self.message_received.emit(self.message)
            self.sendMusic(songid)
        elif "ADD_TO_FAVORITE" in signal:
            data = signal.replace("ADD_TO_FAVORITE_","")
            self.message_received.emit(self.message)
            lstdata = data.split("_")
            userid = lstdata[0]
            songid=lstdata[1]
            self.addToFAV(userid,songid)
        elif "ADD_TO_PLAYLIST" in signal:
            data = signal.replace("ADD_TO_PLAYLIST_","")
            self.message_received.emit(self.message)
            lstdata = data.split("_")
            id = lstdata[0]
            songid=lstdata[1]
            self.addPlayList(id,songid)
        elif "REMOVE_TO_FAVORITE" in signal:
            data = signal.replace("REMOVE_TO_FAVORITE_","")
            self.message_received.emit(self.message)
            lstdata = data.split("_")
            userid = lstdata[0]
            songid=lstdata[1]
            self.removeToFAV(userid,songid)

        elif "REMOVE_TO_PLAYLIST" in signal:
            data = signal.replace("REMOVE_TO_PLAYLIST_","")
            self.message_received.emit(self.message)
            lstdata = data.split("_")
            userid = lstdata[0]
            songid=lstdata[1]
            self.removePlayList(userid,songid)
        elif "ADD_PLAYLIST" in signal:
            data = signal.replace("ADD_PLAYLIST_","")
            self.message_received.emit(self.message)
            lstdata = data.split("_")
            id = lstdata[0]
            userid=lstdata[1]
            title=lstdata[2]
            self.addNewPlayList(id,userid,title)

        elif "UPDATE_TO_USER" in signal:
            data = signal.replace("UPDATE_TO_USER_","")
            self.message_received.emit(self.message)
            lstdata = data.split("_")
            username=lstdata[0]
            name=lstdata[1]
            password=lstdata[2]
            self.updateUser(username,name,password)
        elif "logged" in signal:
            self.message_received.emit(self.message)
        elif signal ==  "GET_USER_LIST":
            self.sendUserLIST()
            
        self.clientSocket.close()