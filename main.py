from client.chat_client import ChatClient
from gui.chat_gui import ChatGUI
from server.chat_server import ChatServer

if __name__ == "__main__":
    nickname = input("Nickname: ")
    host = "127.0.0.1"
    port = 8000
    server = ChatServer(host, port)
    server.start()
    client = ChatClient(nickname=nickname, host=host, port=port)
    gui = ChatGUI(client)
    client.connect_client()
    gui.start_gui()