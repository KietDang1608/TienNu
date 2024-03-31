from GetDataFromServer import GetDataFromServer

client = GetDataFromServer()
client.connect()
lst =  client.sendSignal("GET_FAVORITE_LIST_kietdang")
for i in lst:
    print(i)