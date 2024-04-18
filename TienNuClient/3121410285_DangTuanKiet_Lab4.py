import mysql.connector
import datetime

def connect_sql():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'lab04_1',
        'raise_on_warnings': True
    }
    connection = mysql.connector.connect(**config)
    return connection

def delete(id, con):
    cursor = con.cursor()
    count = cursor.execute("delete from employee where employeeid=%s",(id,))
    con.commit()
    cursor.close()
    if (count>0):
        print("Xóa thành công")
    else:
        print("Mã không tồn tại")
def insert(id,name,birthday, phone,con):
    cursor = con.cursor()
    cursor.execute("insert into employee values(%s,%s,%s,%s)",(id,name,birthday,phone))
    con.commit()
    cursor.close()
def update(id, name,birthday, phone, con):
    cursor = con.cursor()
    cursor.execute("update employee set fullname = %s , birthday = %s , phone = %s where id = %s ",(name,birthday,phone,id))
    con.commit()
    cursor.close()

def findByName(name,con):
    lst = []
    cursor = con.cursor()
    cursor.execute("Select * from employee where fullname like N'%"+"%s" + "%'" , (name))
    rows = cursor.fetchall()
    for row in rows:
        lst.append(row)
    return lst
def selectAll(con):
    lst = []
    cursor = con.cursor()
    cursor.execute("Select * from employee")
    rows = cursor.fetchall()
    for row in rows:
        lst.append(row)
    return lst
def inputEmployee():
    id = str(input("Nhập mã nhân viên: "))
    name = str(input("Nhập tên nhân viên: "))
    birthday = str(input("Nhập ngày sinh(yyyy-mm-dd): "))
    phone = str(input("Điện thoại: "))
    insert(id,name,birthday,phone)
    
def main():
    con = connect_sql()
    while True:
        print("1. Nhập nhân viên")
        print("2. Hiển thị tất cả nhân viên")
        print("3. Xóa nhân viên")
        print("4. Sửa nhân viên")
        print("5. Tìm nhân viên theo tên")
        print("6.THoát")
        choose  = str(input("chọn chức năng: "))
        if (choose == "1"):
            inputEmployee()
        elif choose == "2":
            lst = selectAll()
            for nv in lst:
                print("id: " + nv[0])
                print("name: " + nv[1])
                print("birthday: " + nv[2])
                print("phone: " + nv[3])
        elif choose == "3":
            idnv = str(input("Nhập mã cần xóa"))
            delete(id,con)
        elif choose == "4":
            idnv = str(input("Nhập id của nv cần sửa: "))
            name = str(input("Nhập tên nhân viên: "))
            birthday = str(input("Nhập ngày sinh(yyyy-mm-dd): "))
            phone = str(input("Điện thoại: "))
            update(idnv,name,birthday,phone,con)
        elif choose == "5":
            lst = []
            name = str(input("Nhập tên cần tìm:"))
            lst = findByName(name,con)
            for nv in lst:
                print("id: " + nv[0])
                print("name: " + nv[1])
                print("birthday: " + nv[2])
                print("phone: " + nv[3]) 
        else:
            break
main()
            
            
    