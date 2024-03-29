from FavoriteDAO import FavoriteDAO
class FavoriteBUS:
    def __init__(self):
        self.favoriteDAO = FavoriteDAO()
        self.lstFavorite = self.favoriteDAO.readData()
    def getData(self):
        return self.lstFavorite
    def getFavSongsOfUser(self,userID):
        lst = []
        for fav in self.lstFavorite:
            if fav.userID == userID:
                lst.append(fav)
        return lst
    
