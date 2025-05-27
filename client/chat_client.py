"""
This class represents a client for the user to use for the chat program
it connects to a server and sends messages to it
author: Matthias Baidinger
"""

import socket
import threading

class ChatClient:
    def __init__(self, host, port, nickname):
        self.__host = host
        self.__port = port
        self.__nickname = nickname
        self.__gui = None
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connected = False

    def set_gui(self, value):
        self.__gui = value

    def get_nickname(self):
        return self.__nickname

    def connect_client(self):
        """
        connects the client to a listening server and sends a message that the client has entered the chat
        :return:
        """
        try:
            self.__client_socket.connect((self.__host, self.__port))
            self.__connected = True # client is connected
            threading.Thread(target=self.receive_messages, daemon=True).start()
            self.send_message(f"{self.__nickname} has entered the chat.")
        except (socket.error, socket.herror, socket.gaierror, socket.timeout) as se:
            print(f"Socket error: {se}")
        except Exception as e:
            print(f"Error occurred during client connection: {e}")

    def  send_message(self, message):
        """
        Sends a chat message to the server
        :param message: chat message entered by the user
        :return:
        """
        try:
            message = f"{self.__nickname}:{message}" # attach nickname to message
            self.__client_socket.send(message.encode("UTF-8"))

        except (socket.error, socket.herror, socket.gaierror, socket.timeout) as se:
            print(f"Socket error in send message: {se}")

        except Exception as e:
            print(f"Error occurred during send message: {e}")


    def receive_messages(self):
        """
        Waits for new messages from other clients as long as this client is connected, runs in a thread
        sends message to the gui for display
        :return:
        """
        while self.__connected:
            try:
                message = self.__client_socket.recv(1024).decode('utf-8')

                if message:
                    print(f"\n{message}")
                    self.__gui.display_message(message)

            except Exception as e:
                print(f"Error occurred during receiving messages: {e}")
                break
        #print("DISCONNECTED")
        self.disconnect()

    def disconnect(self):
        """
        disconnects the client from the server, announces in the chat that the client has left
        :return:
        """
        if self.__connected:
            self.__connected = False
            try:
                message = f"{self.__nickname} has left the chat"
                self.send_message(message)
            except Exception as e:
                print(f"Error occurred during disconnect: {e}")

            print(f"{self.__client_socket} connection closed")
