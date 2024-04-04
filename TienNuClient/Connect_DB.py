import mysql.connector

def getConnection():
    # Thay đổi thông tin kết nối dưới đây theo cài đặt của bạn
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'chidepmp3',
        'raise_on_warnings': True
    }
    try:
        # Kết nối đến cơ sở dữ liệu
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Kết nối thành công với MySQL Server", db_Info)
            return connection
    except mysql.connector.Error as e:
        print("Lỗi kết nối:", e)
        return None

    return None
def hello():
    print("Hello")
