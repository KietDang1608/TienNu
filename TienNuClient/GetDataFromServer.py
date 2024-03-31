import socket
import json
class GetDataFromServer():
    ip = 'localhost'
    port = 3306
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
    #Gui tin hieu va nhan lai ket qua
    def sendSignal(self, signal):
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
    def getCategoryList(self):
        try:
            if self.socket:
                received_data = self.receive_and_parse_json_data(self.socket)
                
                return received_data
            else:
                print("Socket connection not established.")
                return None
        except Exception as e:
            print(f"Error receiving data: {e}")
            return None
