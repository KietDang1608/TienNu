import Category_DAO
from Category import Category
class Category_BUS():
    def __init__(self):
        self.lstCategory = Category_DAO.readData()
    def getData(self):
        return self.lstCategory
    def addData(self,cat:Category):
        Category_DAO.addData(cat)
    def editData(self,cat:Category):
        Category_DAO.editData(cat)
    def delData(self,cat:Category):
        Category_DAO.delData(cat)