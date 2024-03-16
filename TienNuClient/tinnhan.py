import socket
import threading

def receive_data(server_socket):
    while True:
        data = server_socket.recv(1024).decode()
        print("Server:", data)
        if data.lower() == "exit":
            break

def send_data(server_socket):
    while True:
        message = input("Client: ")
        server_socket.sendall(message.encode())
        if message.lower() == "exit":
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.8', 5000))

receive_thread = threading.Thread(target=receive_data, args=(client_socket,))
send_thread = threading.Thread(target=send_data, args=(client_socket,))
receive_thread.start()
send_thread.start()
