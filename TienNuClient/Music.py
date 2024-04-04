class Music:
    def __init__(self, id:str, catID:str, name:str, artist:str, img:str, mp3:str,luotNghe=0):
        self.id = id
        self.catID = catID
        self.name = name
        self.artist = artist
        self.img = img
        self.mp3 = mp3
        self.luotNghe = luotNghe
    def to_dict(self):
        return {"id": self.id,"catID":self.catID,"Name":self.name,"artist":self.artist,"img":self.img,"mp3":self.mp3,"LuotNghe:":self.luotNghe }
    
        