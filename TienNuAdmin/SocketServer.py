from Category_BUS import Category_BUS
from NhacBUS import NhacBUS
from FavoriteBUS import FavoriteBUS
import socket
import json
class SocketServer:
    ip = 'localhost'
    port = 3306
    def __init__(self):
        self.host = SocketServer.ip
        self.port = SocketServer.port
        self.serverSocket = None
        self.clientSocket = None
        self.clientAddress = None
    def startServer(self):
        try:
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSocket.bind((self.host, self.port))
            self.serverSocket.listen(1)
            print(f"Server is listening on {self.host}: {self.port}")
            self.clientSocket, self.clientAddress = self.serverSocket.accept()
            print(f"Connection established with {self.clientAddress}")
        except Exception as e:
            print (f'Error starting server: {e}')
    def stopServer(self):
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
    # Hàm nhận tín hiệu gửi từ client, xem tín hiệu là gì tùy trường hợp mà gửi lại dữ liệu tương ứng
    def getSignal(self):
        signal = self.clientSocket.recv(1024).decode("utf-8")
        print( "Tin hieu tu client: ",signal)
        if (signal == "GET_CATEGORY_LIST"):
            self.sendCategoryLIST()
        elif signal == "GET_MUSIC_LIST":
            self.sendMusicLIST()
        elif "GET_FAVORITE_LIST" in signal:
            userid = signal.replace("GET_FAVORITE_LIST_","")
            self.sendFavoriteLIST(userid)
        