
from PyQt6.QtCore import QThread,pyqtSignal
import socket

class Server(QThread):
    stopped = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True
        HOST = '127.0.0.1'
        PORT = 3306
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print(f"Server is listening on {HOST}:{PORT}")
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print('Received:', data.decode())
        self.stopped.emit()  # Gửi tín hiệu khi dừng

    def stop(self):
        self.running = False