import Connect_DB
from Music import Music
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
                music = Music(row[0],row[1],row[2],row[3],row[4],row[5],row[6],)
                lstMusic.append(music)

        except mysql.connector.Error as e:
            print("Lỗi truy vấn:", e)

        finally:
            
            # Đóng cursor và kết nối
            if 'cursor' in locals():
                cursor.close()
            if connection.is_connected():
                connection.close()
                print("Đã đóng kết nối")
            return lstMusic
    else:
        print("Không thể kết nối đến cơ sở dữ liệu.")
def addData(music:Music):
    connection = Connect_DB.getConnection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO music(category,name,artist,img, file) VALUE(%s,%s,%s,%s,%s)",(music.catID,music.name,music.artist,music.img,music.mp3))
        connection.commit()
        cursor.close()
        connection.close()
def editData(music:Music):
    connection = Connect_DB.getConnection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("UPDATE music set category = %s, name = %s, artist = %s, img = %s, file = %s where id = %s",(music.catID,music.name,music.artist,music.img,music.mp3,music.id,))
        connection.commit()
        cursor.close()
        connection.close()
def delData(id):
    connection = Connect_DB.getConnection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("DELETE from music where id = %s",(id,))
        connection.commit()
        cursor.close()
        connection.close()