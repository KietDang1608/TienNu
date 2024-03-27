import Connect_DB
from Slide import Slide, SlideDetail
import mysql.connector
class SlideDAO:
    def __init__(self):
        pass
    def getData(self):
        connection = Connect_DB.getConnection()
        lstSlide = [];
        if connection is not None:
            try:
                # Tạo một đối tượng cursor
                cursor = connection.cursor()

                # Thực hiện truy vấn SQL
                cursor.execute("SELECT * FROM slide")

                # Lấy tất cả các dòng kết quả
                rows = cursor.fetchall()

                # In kết quả
                for row in rows:
                    slide = Slide(row[0],row[1])
                    lstSlide.append(slide)

            except mysql.connector.Error as e:
                print("Lỗi truy vấn:", e)

            finally:
                # Đóng cursor và kết nối
                if 'cursor' in locals():
                    cursor.close()
                if connection.is_connected():
                    connection.close()
                    print("Đã đóng kết nối")
                return lstSlide
        else:
            print("Không thể kết nối đến cơ sở dữ liệu.")
    def addData(self, slide: Slide):
        try:
            connection = Connect_DB.getConnection()
            if connection is not None:
                cursor = connection.cursor()
                sql = f"INSERT into slide(slideTitle) value(%s)"
                value = (slide.slideTitle,)
                cursor.execute(sql,value)
                connection.commit()
        except mysql.connector.Error as e:
            print("Lỗi truy vấn:", e)
        finally:
            if 'cursor' in locals():
                    cursor.close()
            if connection.is_connected():
                connection.close()
                print("Đã đóng kết nối")        
class SlideDetailDAO:
    def __init__(self):
        pass
    def getData(self,slideID):
        connection = Connect_DB.getConnection()
        lstSlideDetail = [];
        if connection is not None:
            try:
                # Tạo một đối tượng cursor
                cursor = connection.cursor()
                sql = "SELECT * FROM slidedetail where slideID = %s"
                val = (slideID,)
                # Thực hiện truy vấn SQL
                cursor.execute(sql,val)

                # Lấy tất cả các dòng kết quả
                rows = cursor.fetchall()

                # In kết quả
                for row in rows:
                    slideDetail = SlideDetail(row[0],row[1])
                    lstSlideDetail.append(slideDetail)

            except mysql.connector.Error as e:
                print("Lỗi truy vấn:", e)

            finally:
                # Đóng cursor và kết nối
                if 'cursor' in locals():
                    cursor.close()
                if connection.is_connected():
                    connection.close()
                    print("Đã đóng kết nối")
                return lstSlideDetail
        else:
            print("Không thể kết nối đến cơ sở dữ liệu.")
    def addData(self, slideDetail:SlideDetail):
        try:
            connection = Connect_DB.getConnection()
            if connection is not None:
                cursor = connection.cursor()
                sql = f"INSERT into slidedetail(slideid,songid) value(%d,%d)"
                value = (slideDetail.slideid,slideDetail.songid,)
                cursor.execute(sql,value)
                connection.commit()
        except mysql.connector.Error as e:
            print("Lỗi truy vấn:", e)
        finally:
            if 'cursor' in locals():
                    cursor.close()
            if connection.is_connected():
                connection.close()
                print("Đã đóng kết nối")        
