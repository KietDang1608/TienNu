import MusicDAO
from Music import Music
class NhacBUS():
    def __init__(self):
        self.lstNhac = MusicDAO.readData()
    def getData(self):
        return self.lstNhac
    def getMusicByID(self, musicid:int):
        for music in self.lstNhac:
            if music.id == musicid:
                return music
    def addSong(self, song:Music):
        MusicDAO.addData(song)
    def updateSong(self,song:Music):
        MusicDAO.editData(song)
    def delData(self,id):
        MusicDAO.delData(id)
    def findSongByID(self, data:str):
        
        lstFound = []
        for music in self.lstNhac:
            text = str(music.id)
            if data in text:
                lstFound.append(music)
        return lstFound
    def getMP3FileByID(self,id:str):
        for music in self.lstNhac:
            musicid = str(music.id)
            if (id == musicid):
                return music.mp3
        return ""
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