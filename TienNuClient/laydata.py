import socket
import json

class Music:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

def receive_and_parse_json_data(client_socket):
    received_data = b""
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        received_data += chunk
    data_list = json.loads(received_data.decode())  # Chuyển đổi chuỗi JSON thành danh sách
    return data_list

def send_request_to_server():
    # Tạo socket và kết nối
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 3306))

    # Nhận và chuyển đổi dữ liệu
    received_data = receive_and_parse_json_data(client_socket)

    print("Received data:")
    for item in received_data:
        print(item)

    client_socket.close()

# Gửi yêu cầu cho server để nhận dữ liệu
send_request_to_server()
