from User import User
from UserDAO import UserDAO
class UserBUS:
    def __init__(self):
        self.userDAO = UserDAO()
        self.lstUser = self.userDAO.readData()
    def readData(self):
        return self.lstUser
    def addData(self,username,password,name):
        self.userDAO.addData(username,password,name)
    def updateUser(self,password,name,username):
        self.userDAO.updateUser(password,name,username)
    def getUserByID(self,username:str):
        lst = []
        for item in self.lstUser:
            if item.username == username:
                lst.append(item)
        return lst
        
    