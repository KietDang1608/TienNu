import Connect_DB
from User import User
import mysql.connector
class UserDAO:
    def __init__(self):
        pass
    
    def readData(self):
        connection = Connect_DB.getConnection()
        lstUser = [];
        if connection is not None:
            try:
                # Tạo một đối tượng cursor
                cursor = connection.cursor()

                # Thực hiện truy vấn SQL
                cursor.execute("SELECT * FROM user")

                # Lấy tất cả các dòng kết quả
                rows = cursor.fetchall()

                # In kết quả
                for row in rows:
                    user = User(row[0],row[1],row[2],row[3])
                    lstUser.append(user)

            except mysql.connector.Error as e:
                print("Lỗi truy vấn:", e)

            finally:
                # Đóng cursor và kết nối
                if 'cursor' in locals():
                    cursor.close()
                if connection.is_connected():
                    connection.close()
                    print("Đã đóng kết nối")
                return lstUser
        else:
            print("Không thể kết nối đến cơ sở dữ liệu.")
    def addData(self, user:User):
        try:
            connection = Connect_DB.getConnection()
            if connection is not None:
                cursor = connection.cursor()
                sql = f"INSERT into user value({user.username},{user.password},{user.name},{user.datecreate})"
                cursor.execute(sql)
                connection.commit()
        except mysql.connector.Error as e:
            print("Lỗi truy vấn:", e)
        finally:
            if 'cursor' in locals():
                    cursor.close()
            if connection.is_connected():
                connection.close()
                print("Đã đóng kết nối")        