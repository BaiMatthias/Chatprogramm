from client import ChatClient
from gui import ChatGUI


if __name__ == "__main__":
    nickname = input("Nickname: ")
    host = "127.0.0.1"
    port = 8000

    client = ChatClient(nickname=nickname, host=host, port=port)
    gui = ChatGUI(client)
    client.set_gui(gui)
    client.connect_client()
    gui.start_gui()