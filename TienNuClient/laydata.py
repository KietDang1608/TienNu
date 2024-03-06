import requests

def get_data_from_server():
    url = 'http://127.0.0.1:5000/data'  # Thay 'your_server_endpoint' bằng URL của ứng dụng server của bạn
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Dữ liệu từ máy chủ:")
            print(data)
        else:
            print("Không thể lấy dữ liệu từ máy chủ. Mã trạng thái:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Lỗi khi gửi yêu cầu:", e)

if __name__ == "__main__":
    get_data_from_server()