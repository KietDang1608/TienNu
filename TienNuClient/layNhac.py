import sys
import socket
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QByteArray
import numpy as np
import sounddevice as sd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 300, 200)

        self.button1 = QPushButton("Play Song 1", self)
        self.button1.setGeometry(50, 50, 200, 50)
        self.button1.clicked.connect(lambda: self.request_audio_data(1))

        self.button2 = QPushButton("Play Song 2", self)
        self.button2.setGeometry(50, 120, 200, 50)
        self.button2.clicked.connect(lambda: self.request_audio_data(2))

        self.server_address = ('localhost', 3306)  # Địa chỉ và cổng của máy chủ

    def request_audio_data(self, song_id):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect(self.server_address)
                request = f"PLAY {song_id}"
                client_socket.sendall(request.encode())

            # Nhận dữ liệu âm thanh từ máy chủ
                audio_data = bytearray()
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    audio_data += data

            # Kiểm tra định dạng và nội dung của dữ liệu âm thanh
                print("Received audio data:", audio_data)
                print("Length of audio data:", len(audio_data))

            # Phát âm thanh từ dữ liệu nhận được
                self.play_music(audio_data)
        except ConnectionRefusedError:
            print("Cannot connect to the server.")
    def play_music(self, audio_data):
        try:
            # Chuyển dữ liệu âm thanh thành mảng numpy
            audio_array = np.frombuffer(audio_data, dtype=np.int16)

            # Phát âm thanh từ mảng numpy
            sd.play(audio_array, samplerate=44100)
            sd.wait()
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
