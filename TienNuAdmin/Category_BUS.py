import Category_DAO

class Category_BUS():
    def __init__(self):
        self.lstCategory = Category_DAO.readData()
    def getData(self):
        return self.lstCategory
