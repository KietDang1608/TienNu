import socket
# Tạo một socket object

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Kết nối tới địa chỉ và cổng của server
server_address = ('127.0.0.1', 3306)
client_socket.connect(server_address)