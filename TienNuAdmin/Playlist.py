class Playlist:
    def __init__(self,id:str, userid:str, title:str):
        self.id = id
        self.userID = userid
        self.title = title
    def toString(self):
        return f"ID: {self.id}, UserID: {self.userID}, Title: {self.title}"

class PlaylistDetail:
    def __init__(self, playlistID:str,songid:str):
        self.playlistID = playlistID
        self.songid = songid
    def toString(self):
        return f"PlaylistID: {self.playlistID}, SongID: {self.songid}"
    
        
        
        
        