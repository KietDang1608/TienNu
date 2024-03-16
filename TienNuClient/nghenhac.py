import socket
import tempfile
import pygame

def getMusic(id:int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 3306)  # Change to match server address and port

    try:
        client_socket.connect(server_address)

        pygame.init()
        pygame.mixer.init()
        
        client_socket.sendall(str(id).encode())

        # Create a temporary file-like object to store the received audio data
        temp_audio_file = tempfile.SpooledTemporaryFile(max_size=10000000)  # Adjust max_size as needed

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            temp_audio_file.write(data)

        # Move the file pointer to the beginning of the temporary file
        temp_audio_file.seek(0)

        # Load the temporary file as music
        pygame.mixer.music.load(temp_audio_file)

        # Play the loaded music
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    finally:
        client_socket.close()

if __name__ == "__main__":
    getMusic(2)
