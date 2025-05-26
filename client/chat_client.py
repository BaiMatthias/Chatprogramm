import socket
import threading

class ChatClient:
    def __init__(self, host, port, nickname, gui):
        self.__host = host
        self.__port = port
        self.__nickname = nickname
        self.__gui = gui
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connected = False


    def connect_client(self):
        try:
            self.__client_socket.connect((self.__host, self.__port))
            self.__connected = True # client is connected
            threading.Thread(target=self.receive_messages, daemon=True).start()
            # self.send(f"{self.nickname} hat den Chat betreten.")
        except Exception as e:
            print(f"Error occurred during client connection: {e}")

    def  send_message(self, message):
        try:
            self.__client_socket.send(message.encode("UTF-8"))
        except Exception as e:
            print(f"Error occurred during send message: {e}")
            self.disconnect()

    def receive_messages(self):
        while self.__connected:
            try:
                message = self.__client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"\n{message}")
                    self.__gui.display(message)

                else:
                    break
            except Exception as e:
                print(f"Error occurred during receiving messages: {e}")
                break

        self.disconnect()

    def disconnect(self):
        if self.__connected:
            self.__connected = False
            try:
                message = f"{self.__nickname} has left the chat"
                self.send_message(message)
            except Exception as e:
                print(f"Error occurred during disconnect: {e}")

            print(f"{self.__client_socket} connection closed")
