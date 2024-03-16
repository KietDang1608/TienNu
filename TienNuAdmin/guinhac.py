import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 3306)  # Change to your desired address and port
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Server is listening on", server_address)

    while True:
        connection, client_address = server_socket.accept()
        print("Connection from", client_address)

        try:
            # Receive the ID from the client
            client_id = int(connection.recv(1024).decode())  # Convert to integer
            if client_id == 2:
                with open("C:\\Users\\KietDang\\Documents\\PYTHON\\TienNu\\TienNuAdmin\\song\\tabun.mp3", "rb") as music_file:
                    data = music_file.read(1024)
                    while data:
                        connection.sendall(data)
                        data = music_file.read(1024)
            # Check if the ID matches the expected value
            if client_id == 1:  # Change the expected ID as needed
                # Load and send the audio file
                with open("C:\\Users\\KietDang\\Documents\\PYTHON\\TienNu\\TienNuAdmin\\song\\test.mp3", "rb") as music_file:
                    data = music_file.read(1024)
                    while data:
                        connection.sendall(data)
                        data = music_file.read(1024)
        finally:
            connection.close()

if __name__ == "__main__":
    filename = "music.mp3"  # Default filename
    main()
