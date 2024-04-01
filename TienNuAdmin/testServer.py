from SocketServer import SocketServer

socketServer = SocketServer()

socketServer.startServer()
while True:
    socketServer.getSignal()