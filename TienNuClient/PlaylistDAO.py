import Connect_DB
from Playlist import Playlist,PlaylistDetail
import mysql.connector
class PlaylistDAO:
    def __init__(self):
        pass
    
    def readData(self):
        connection = Connect_DB.getConnection()
        lstPlaylist = [];
        if connection is not None:
            try:
                # Tạo một đối tượng cursor
                cursor = connection.cursor()

                # Thực hiện truy vấn SQL
                cursor.execute("SELECT * FROM playlist")

                # Lấy tất cả các dòng kết quả
                rows = cursor.fetchall()

                # In kết quả
                for row in rows:
                    playlist = Playlist(row[0],row[1],row[2],)
                    lstPlaylist.append(playlist)

            except mysql.connector.Error as e:
                print("Lỗi truy vấn:", e)

            finally:
                
                # Đóng cursor và kết nối
                if 'cursor' in locals():
                    cursor.close()
                if connection.is_connected():
                    connection.close()
                    print("Đã đóng kết nối")
                return lstPlaylist
        else:
            print("Không thể kết nối đến cơ sở dữ liệu.")
class PlaylistDetailDAO:
    def __init__(self):
        pass
    
    def readData(self):
        connection = Connect_DB.getConnection()
        lstdetail = [];
        if connection is not None:
            try:
                # Tạo một đối tượng cursor
                cursor = connection.cursor()

                # Thực hiện truy vấn SQL
                cursor.execute("SELECT * FROM playlistdetail")

                # Lấy tất cả các dòng kết quả
                rows = cursor.fetchall()

                # In kết quả
                for row in rows:
                    detail = PlaylistDetail(row[0],row[1],)
                    lstdetail.append(detail)

            except mysql.connector.Error as e:
                print("Lỗi truy vấn:", e)

            finally:
                
                # Đóng cursor và kết nối
                if 'cursor' in locals():
                    cursor.close()
                if connection.is_connected():
                    connection.close()
                    print("Đã đóng kết nối")
                return lstdetail
        else:
            print("Không thể kết nối đến cơ sở dữ liệu.")
