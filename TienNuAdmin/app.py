import socket
import json
from NhacBUS import NhacBUS
class Music:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

def send_data(client_socket, data):
    # Chuyển đổi danh sách các đối tượng từ lớp Music thành danh sách các từ điển
    data_dict = [vars(obj) for obj in data]
    # Chuyển đổi danh sách các từ điển thành chuỗi JSON
    json_data = json.dumps(data_dict)
    # Gửi dữ liệu dưới dạng JSON
    client_socket.sendall(json_data.encode())

def run_server():
    print("Đang chạy server")
    # Tạo socket và kết nối
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 3306))
    server_socket.listen(1)

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        nhacBUS = NhacBUS()
        # Tạo danh sách các đối tượng từ lớp Music
        music_list = nhacBUS.getData()

        # Gửi danh sách các đối tượng từ lớp Music dưới dạng JSON
        send_data(client_socket, music_list)

        client_socket.close()

# Chạy server
run_server()
