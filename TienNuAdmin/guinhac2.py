import socket

def send_audio_data(client_socket, filename):
    try:
        with open(filename, "rb") as audio_file:
            while True:
                data = audio_file.read(1024)
                if not data:
                    break
                client_socket.send(data)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 3306)  # Địa chỉ và cổng của máy chủ
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Server is listening on", server_address)

    while True:
        connection, client_address = server_socket.accept()
        print("Connection from", client_address)

        try:
            # Nhận yêu cầu từ máy khách
            request = connection.recv(1024).decode()

            # Xử lý yêu cầu
            if request.startswith("PLAY"):
                song_id = int(request.split()[1])  # Lấy ID bài hát từ yêu cầu
                if song_id == 1:
                    filename = f"song{song_id}.mp3"   # Tên tệp nhạc dựa trên ID
                    send_audio_data(connection, "C:\\Users\\KietDang\\Documents\PYTHON\\TienNu\\TienNuAdmin\\song\\tabun.mp3")
                else:
                    send_audio_data(connection, "C:\\Users\\KietDang\\Documents\PYTHON\\TienNu\\TienNuAdmin\\song\\test.mp3")

        finally:
            connection.close()

if __name__ == "__main__":
    main()
