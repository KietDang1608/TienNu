from PlaylistDAO import *
class PlaylistBUS:
    def __init__(self):
        dao = PlaylistDAO()
        self.lstPlaylist = dao.readData()
    def getData(self):
        return self.lstPlaylist
    def getPLaylistByUserID(self,userID:str):
        lst = []
        for item in self.lstPlaylist:
            if item.userID == userID:
                lst.append(item)
        return lst

        
class PlayListDetailBUS:
    def __init__(self):
        self.dao = PlaylistDetailDAO()
        self.lstPlaylistDetail = self.dao.readData()
    def getData(self):
        return self.lstPlaylistDetail
    def getPlayListByID(self,id:str):
        lst = []
        for item in self.lstPlaylistDetail:
            
            if str(item.playlistID) == id:
                
                lst.append(item)
        return lst
    def addData(self,id,songid):
        self.dao.addData(id,songid)
            
        