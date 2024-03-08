from flask import Flask, send_file
import os
app = Flask(__name__)

# Đường dẫn tới thư mục chứa các tệp nhạc
MUSIC_DIRECTORY = "TienNuAdmin\\song\\"

@app.route("/song",methods=['GET'])
def get_music():
    # Xác định đường dẫn tuyệt đối của tệp nhạc
    music_path = os.path.join(MUSIC_DIRECTORY, "test.mp3")
    # Kiểm tra xem tệp nhạc có tồn tại không
    if os.path.exists(music_path):
        # Trả về tệp nhạc cho client
        return send_file(music_path)
    else:
        # Trả về mã lỗi 404 nếu không tìm thấy tệp nhạc
        return "File not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
