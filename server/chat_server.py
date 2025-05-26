"""
This class represents a server for the chat program.
It manages its clients and starts processes to receive and forward messages to other clients
"""

import socket
import threading


class ChatServer:

    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__clients = []

    def start(self):
        """
        Starts the server and listens to the host and port for clients to connect
        :return:
        """
        self.__server_socket.bind((self.__host, self.__port))
        self.__server_socket.listen()
        print(f"Server was started and is active on {self.__host} and port {self.__port}")
        self.__accept_clients()



    def __accept_clients(self):
        """
        Accepts the connection request of a new client and add it to its internal list to keep track of it
        Starts a process for each new connected client
        :return:
        """
        while True:
            client_socket, client_address = self.__server_socket.accept()
            print(f"connected to client {client_address}")
            self.__clients.append(client_socket)
            threading.Thread(target=self.manage_client, args=(client_socket,), daemon=True).start()

    def manage_client(self, client_socket):
        """
        Process for receiving messages from a client and forwarding it to all other clients except the one
        sending it
        :param client_socket: The client from which messages are received
        :return:
        """
        while True:
            try:
                message  = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"test: {message}")
                    self.send_messages(message,client_socket)
                else:
                    break
            except:
                break # Fehlerhandling noch machen

        print(f"Client {client_socket} disconnected")
        self.__clients.remove(client_socket)
        client_socket.close()

    def send_messages(self, message, sender):
        """
        Sends the received message to all other clients except the one sending it
        :param message: The message to forward
        :param sender: the sender of the message
        :return:
        """
        for client in self.__clients:
            if client != sender:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    client.close()
                    self.__clients.remove(client)




