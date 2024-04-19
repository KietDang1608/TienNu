from GetDataFromServer import GetDataFromServer
import pygame
import demo
client = GetDataFromServer()
client.connect()

# lst =  client.sendSignal("GET_SONGS_OF_PLAYLIST_1")
# for i in lst:
#     print(i)
userid = "minhhuu"

while True:
    print("1. Get list category")    
    print("2. Get list music")
    print("3. Get list playlist")
    print("4. Get songs of playlist")
    print("5. Play song 1")
    print("6. Get my favorite songs")
    print("7. add to fav")
    print("8.Get user List")
    print("0. Thoat")
    lst = []
    choice = int(input("Nhap lua chon: "))
    if choice == 1:
        lst = client.sendSignal("GET_CATEGORY_LIST")
        for item in lst:
            print(item)
    elif choice == 2:
        lst = client.sendSignal("GET_MUSIC_LIST")
        for item in lst:
            print(item)
    elif choice == 3:
        print("My playlist list: ")
        lst = client.sendSignal("GET_PLAYLIST_LIST_" + userid)
        for item in lst:
            print(item)
    elif choice == 4:
        playlistid = str(input("Nhap ma playlist: "))
        lst = client.sendSignal("GET_SONGS_OF_PLAYLIST_" + playlistid)
        for item in lst:
            print(item)
    elif choice == 5:
        song = str(input("Nhap id: "))
        client.playSongFromServer(song)
    elif choice == 6:
        lst = client.sendSignal("GET_FAVORITE_LIST_" + userid)
        for item in lst:
            print(item)
    elif choice == 7:
        songid = str(input("Nhap nhac can them: "))
        receive = client.sendAddToFavorite("ADD_TO_FAVORITE_" + userid + "_" + songid)
        print(receive)
    elif choice == 9:
        songid = str(input("Nhap nhac can them: "))
        receive = client.sendAddToPlaylist("ADD_TO_PLAYLIST_" + "3" + "_" + songid)
        print(receive)
    elif choice == 8:
        print("User list: ")
        lst = client.sendSignal("GET_USER_LIST")
        for item in lst:
            print(item)
    else:
        break