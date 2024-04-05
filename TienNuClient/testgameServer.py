import socket
import threading
import pickle
import random
from circle import Circle
# Class đại diện cho một client
class Client:
    def __init__(self, socket, player_number):
        self.socket = socket
        self.player_number = player_number



# Hàm xử lý kết nối từ client
def handle_client(client):
    while True:
        try:
            # Nhận dữ liệu từ client
            data = client.socket.recv(1024)
            if not data:
                print(f"Player {client.player_number} disconnected")
                break

            # Gửi dữ liệu tới tất cả các client khác
            for other_client in clients:
                if other_client != client:
                    other_client.socket.sendall(data)
        except Exception as e:
            print(f"Error: {e}")
            break

# Khởi tạo server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Xác định host và port để lắng nghe kết nối
host = "127.0.0.1"  # localhost
port = 3306

# Gắn kết server socket với host và port
server_socket.bind((host, port))

# Lắng nghe kết nối từ client
server_socket.listen()

# List lưu trữ tất cả các client kết nối đến server
clients = []

print("Server is listening for connections...")

# Vòng lặp chính để chấp nhận kết nối từ client
player_number = 1
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Player {player_number} connected from {client_address}")

    # Tạo một hình tròn ngẫu nhiên cho client
    circle = Circle(random.randint(50, 750), random.randint(50, 550), player_number)
    circle_data = pickle.dumps(circle)

    # Gửi dữ liệu về tọa độ của hình tròn cho client
    client_socket.sendall(circle_data)

    # Tạo một đối tượng Client mới và thêm vào list
    client = Client(client_socket, player_number)
    clients.append(client)

    # Xử lý kết nối của client trong một thread riêng biệt
    threading.Thread(target=handle_client, args=(client,)).start()

    # Tăng số thứ tự của player cho kết nối kế tiếp
    player_number += 1

# Đóng server socket
server_socket.close()
