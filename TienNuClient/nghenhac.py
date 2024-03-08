import pygame
import requests
from io import BytesIO

def play_music_from_server(server_url, filename):
    # Gửi yêu cầu GET đến máy chủ để tải tệp nhạc
    response = requests.get(f"{server_url}/song")

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Khởi tạo pygame
        pygame.init()
        pygame.mixer.init()

        # Tạo buffer từ dữ liệu nhạc
        music_buffer = BytesIO(response.content)

        # Phát nhạc từ buffer
        pygame.mixer.music.load(music_buffer)
        pygame.mixer.music.play()

        # Đợi cho đến khi nhạc kết thúc
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    else:
        print("Không thể tải bài hát từ máy chủ.")

# Gọi hàm play_music_from_server với URL của máy chủ và tên tệp nhạc
server_url = "http://192.168.1.3:5000"
filename = "test.mp3"
play_music_from_server(server_url, filename)
