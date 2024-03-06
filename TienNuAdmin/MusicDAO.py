from ConnectDB import Connect_DB
from DTO.Music import Music
import mysql.connector

def readData():
    connection = Connect_DB.getConnection()
    lstMusic = [];
    if connection is not None:
        try:
            # Tạo một đối tượng cursor
            cursor = connection.cursor()

            # Thực hiện truy vấn SQL
            cursor.execute("SELECT * FROM music")

            # Lấy tất cả các dòng kết quả
            rows = cursor.fetchall()

            # In kết quả
            for row in rows:
                music = Music(row[0],row[1],row[2],row[3],row[4],row[5],)
                lstMusic.append(music)

        except mysql.connector.Error as e:
            print("Lỗi truy vấn:", e)

        finally:
            return lstMusic
            # Đóng cursor và kết nối
            if 'cursor' in locals():
                cursor.close()
            if connection.is_connected():
                connection.close()
                print("Đã đóng kết nối")
    else:
        print("Không thể kết nối đến cơ sở dữ liệu.")
def printData():
    print(readData())
def hello():
    print("hello")
