import socket
import json
import pygame
import tempfile
class GetDataFromServer():
    ip = 'localhost'#My LAN ip:172.20.10.5
    port = 8888
    def __init__(self):
        self.socket = None
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip, self.port))
            print("Connected to server")
        except Exception as e:
            print(f"Connection failed: {e}")
    def close(self):
        if self.socket:
            self.socket.close()
            print("Connection closed")
        else:
            print("No active connection")
    def receive_and_parse_json_data(self,clientSocket):
        received_data = b""
        while True:
            chunk = clientSocket.recv(4096)
            if not chunk:
                break
            received_data += chunk
        data_list = json.loads(received_data.decode())  # Chuyển đổi chuỗi JSON thành danh sách
        return data_list
    def sendAddToFavorite(self,signal):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        try:
            if self.socket:
                self.socket.sendall(signal.encode())
                print(f"Signal {signal} sent successfully!")
                received = self.socket.recv(1024)
                received = received.decode("utf-8")
                return received
            else:
                print("Socket connection not established.")
        except Exception as e:
            print(f"Error sending signal: {e}")
    def sendAddToPlaylist(self,signal):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        try:
            if self.socket:
                self.socket.sendall(signal.encode())
                print(f"Signal {signal} sent successfully!")
                received = self.socket.recv(1024)
                received = received.decode("utf-8")
                return received
            else:
                print("Socket connection not established.")
        except Exception as e:
            print(f"Error sending signal: {e}")
    def sendRemoveFavorite(self,signal):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        try:
            if self.socket:
                self.socket.sendall(signal.encode())
                print(f"Signal {signal} sent successfully!")
                received = self.socket.recv(1024)
                received = received.decode("utf-8")
                return received
            else:
                print("Socket connection not established.")
        except Exception as e:
            print(f"Error sending signal: {e}")
    
    def sendUpdateUser(self,signal):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        try:
            if self.socket:
                self.socket.sendall(signal.encode())
                print(f"Signal {signal} sent successfully!")
                received = self.socket.recv(1024)
                received = received.decode("utf-8")
                return received
            else:
                print("Socket connection not established.")
        except Exception as e:
            print(f"Error sending signal: {e}")


    #Gui tin hieu va nhan lai ket qua
    def sendSignal(self, signal):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        receiveData = b""
        try:
            if self.socket:
                # Gui tin hieu
                self.socket.sendall(signal.encode())
                print(f"Signal '{signal}' sent successfully")
                # nap ket qua vao list
                while True:
                    chunk = self.socket.recv(10000)
                    if not chunk:
                        break
                    receiveData +=chunk
                dataList = json.loads(receiveData.decode())
                return dataList
            else:
                print("Socket connection not established.")
        except Exception as e:
            print(f"Error sending signal: {e}")
    def playSongFromServer(self,songid:str):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        signal = "PLAY_SONG_" + songid
        self.socket.sendall(signal.encode())
        pygame.init()
        pygame.mixer.init()
        temp_audio_file = tempfile.SpooledTemporaryFile(max_size=10000000)  # Adjust max_size as needed

        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            temp_audio_file.write(data)

        # Move the file pointer to the beginning of the temporary file
        temp_audio_file.seek(0)

        # Load the temporary file as music
        pygame.mixer.music.load(temp_audio_file)

        # Play the loaded music
        pygame.mixer.music.play()

        # # Wait for the music to finish playing
        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(10)
        