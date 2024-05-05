import Connect_DB
from User import User
import mysql.connector
from datetime import datetime
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
    def addData(self, username:str,password:str,name:str):
        ngay_hien_tai = datetime.now()
        datecreate= ngay_hien_tai.strftime('%Y-%m-%d')
        try:
            connection = Connect_DB.getConnection()
            if connection is not None:
                cursor = connection.cursor()
                sql = f"INSERT into user value('{username}','{password}','{name}','{datecreate}')"
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

    def updateUser(self, password:str,name:str,username:str):
        try:
            connection = Connect_DB.getConnection()
            if connection is not None:
                cursor = connection.cursor()
                # Tạo câu lệnh SQL để cập nhật thông tin người dùng
                sql = f"UPDATE user SET password = '{password}', name = '{name}' WHERE username = '{username}'"
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