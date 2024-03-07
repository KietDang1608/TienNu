import MusicDAO

class NhacBUS():
    def __init__(self):
        self.lstNhac = MusicDAO.readData()
    def getData(self):
        return self.lstNhac
