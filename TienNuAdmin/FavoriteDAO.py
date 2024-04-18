import Connect_DB
from Favorite import Favorite
import mysql.connector
class FavoriteDAO:
    def __init__(self):
        pass
    
    def readData(self):
        connection = Connect_DB.getConnection()
        lstFavorite = [];
        if connection is not None:
            try:
                # Tạo một đối tượng cursor
                cursor = connection.cursor()

                # Thực hiện truy vấn SQL
                cursor.execute("SELECT * FROM favorites")

                # Lấy tất cả các dòng kết quả
                rows = cursor.fetchall()

                # In kết quả
                for row in rows:
                    favorite = Favorite(row[0],row[1],)
                    lstFavorite.append(favorite)

            except mysql.connector.Error as e:
                print("Lỗi truy vấn:", e)

            finally:
                
                # Đóng cursor và kết nối
                if 'cursor' in locals():
                    cursor.close()
                if connection.is_connected():
                    connection.close()
                    print("Đã đóng kết nối")
                return lstFavorite
        else:
            print("Không thể kết nối đến cơ sở dữ liệu.")

    def addData(self,userid:str,songid:str):
        connection = Connect_DB.getConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO favorites(userID, songID) value(%s,%s)",(userid,songid))
        connection.commit()
        cursor.close()
        connection.close()
    def deleteData(self,userid:str,songid:str):
        connection = Connect_DB.getConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM favorites where userID = %s and songID = %s ", (userid,songid))
        connection.commit()
        cursor.close()
        connection.close()
        