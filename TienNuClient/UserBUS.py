from User import User
from UserDAO import UserDAO
class UserBUS:
    def __init__(self):
        self.userDAO = UserDAO()
        self.lstUser = self.userDAO.readData()
    def readData(self):
        return self.lstUser
    def addData(self,user:User):
        self.userDAO.addData(user)

        
    