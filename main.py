from client.chat_client import ChatClient
from gui.chat_gui import ChatGUI

if __name__ == "__main__":
    nickname = input("Nickname: ")
    host =
    port =
    client = ChatClient(nickname=nickname)
    gui = ChatGUI(client)
    client.connect_client()
    gui.start_gui()