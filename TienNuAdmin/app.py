from flask import Flask, jsonify, send_file

app = Flask(__name__)

# Route cơ bản trả về một danh sách mẫu
@app.route('/data', methods=['GET'])
def get_data():
    sample_data = [
        {"id": 1, "name": "Hữu Khùng"},
        {"id": 2, "name": "Hưng Khùng"},
        {"id": 3, "name": "Đạt Khùng"}
    ]
    return jsonify(sample_data)
MP3_FILE_PATH = 'song/test.mp3'  

@app.route('/music', methods=['GET'])
def stream_music():
    # Trả về file MP3 dưới dạng streaming
    return send_file(MP3_FILE_PATH, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)