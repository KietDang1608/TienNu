import MusicDAO
from Music import Music
class NhacBUS():
    def __init__(self):
        self.lstNhac = MusicDAO.readData()
    def getData(self):
        return self.lstNhac
    def findSongByID(self, data:str):
        
        lstFound = []
        for music in self.lstNhac:
            text = str(music.id)
            if data in text:
                lstFound.append(music)
        return lstFound
    def findSongByCategoryID(self, data:str):
        lstFound = []
        for music in self.lstNhac:
            text = str(music.catID)
            if data == text:
                lstFound.append(music)
        return lstFound
    def findSongByName(self, data:str):
        lstFound = []
        for music in self.lstNhac:
            if data in music.name:
                lstFound.append(music)
        return lstFound
    def findSongByArtist(self, data:str):
        lstFound = []
        for music in self.lstNhac:
            if data in music.artist:
                lstFound.append(music)
        return lstFound