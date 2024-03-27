from SlideDAO import *
from Slide import *

class SlideBUS:
    def __init__(self):
        self.slideDao = SlideDAO()
        self.slides = self.slideDao.getData()
    def getData(self):
        return self.slides
class SlideDetailBUS:
    def __init__(self):
        self.slideDetailDAO = SlideDetailDAO()
        self.slideDetails=[]
    def getData(self,slideid:int):
        self.slideDetails = self.slideDetailDAO.getData(slideid)
        return self.slideDetails
    