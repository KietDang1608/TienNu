class Favorite:
    def __init__(self, userID:str,songID:str):
        self.userID = userID
        self.songID = songID
    def __str__(self):
        return f"{self.userID}, {self.songID}"
        