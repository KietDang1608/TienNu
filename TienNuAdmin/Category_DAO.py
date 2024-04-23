import Connect_DB
from Category import Category
import mysql.connector

def readData():
    connection = Connect_DB.getConnection()
    lstCategory = [];
    if connection is not None:
        try:
            # Tạo một đối tượng cursor
            cursor = connection.cursor()

            # Thực hiện truy vấn SQL
            cursor.execute("SELECT * FROM category")

            # Lấy tất cả các dòng kết quả
            rows = cursor.fetchall()

            # In kết quả
            for row in rows:
                category = Category(row[0],row[1])
                lstCategory.append(category)

        except mysql.connector.Error as e:
            print("Lỗi truy vấn:", e)

        finally:
            return lstCategory
            # Đóng cursor và kết nối
            if 'cursor' in locals():
                cursor.close()
            if connection.is_connected():
                connection.close()
                print("Đã đóng kết nối")
    else:
        print("Không thể kết nối đến cơ sở dữ liệu.")
def printData():
    for cat in readData():
        print(cat.__str__())
def addData(cat:Category):
    connection = Connect_DB.getConnection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO category(title) VALUE(%s)",(cat.title,))
        connection.commit()
        cursor.close()
        connection.close()
def editData(cat:Category):
    connection = Connect_DB.getConnection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("UPDATE category set title = %s where id = %s",(cat.title,cat.id,))
        connection.commit()
        cursor.close()
        connection.close()
def delData(cat:Category):
    connection = Connect_DB.getConnection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM category where id = %s",(cat.id, ))
        connection.commit()
        cursor.close()
        connection.close()
def hello():
    print("hello")

printData()