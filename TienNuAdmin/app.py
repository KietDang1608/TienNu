from flask import Flask, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)