from Category_BUS import Category_BUS
from NhacBUS import NhacBUS
from FavoriteBUS import FavoriteBUS
from PlaylistBUS import PlaylistBUS,PlayListDetailBUS
from PyQt6.QtCore import QThread,pyqtSignal
import pygame
import socket
import json
import os
class SocketServer(QThread):
    message_received = pyqtSignal(str)
    stopped =pyqtSignal()
    ip = 'localhost'
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
                self.message_received.emit(self.message)
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
    # Hàm nhận tín hiệu gửi từ client, xem tín hiệu là gì tùy trường hợp mà gửi lại dữ liệu tương ứng
    def getSignal(self):
        self.clientSocket, self.clientAddress = self.serverSocket.accept()
        print(f"Connection established with {self.clientAddress}")
        signal = self.clientSocket.recv(1024).decode("utf-8")
        print( "Tin hieu tu client: ",signal)
        if (signal == "GET_CATEGORY_LIST"):
            self.message = "Server: SEND CATEGORYLIST"
            self.sendCategoryLIST()
        elif signal == "GET_MUSIC_LIST":
            self.message = "Server: SEND Music list"
            self.sendMusicLIST()
        elif "GET_FAVORITE_LIST" in signal:
            userid = signal.replace("GET_FAVORITE_LIST_","")
            self.message = "Server: SEND Favorite musics for user: " + userid
            self.sendFavoriteLIST(userid)
        elif "GET_PLAYLIST_LIST" in signal:
            userid = signal.replace("GET_PLAYLIST_LIST_","")
            self.sendPlaylistLIST(userid)
        elif "GET_SONGS_OF_PLAYLIST" in signal:
            playlistid = signal.replace("GET_SONGS_OF_PLAYLIST_","")
            self.sendSongsInPlaylist(playlistid)
        elif "PLAY_SONG" in signal:
            songid = signal.replace("PLAY_SONG_","")
            self.sendMusic(songid)
        self.clientSocket.close()