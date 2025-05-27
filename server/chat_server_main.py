from server import ChatServer

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000
    server = ChatServer(host, port)
    server.start()