"""
This class represents a user interface for the chat program
It enables the sending of messages to other clients
It consists of a chat area for displaying chat messages, an input field to enter messages
and a button to send a message
"""
import tkinter as tk
from tkinter import scrolledtext as st
from datetime import datetime


class ChatGUI:
    """
    creates the user interface
    It creates a window in which a scrollable text area for displaying chat messages is created
    in the bottom part of the window there is an input field for entering messages and a button to send the message
    """
    def __init__(self, client):

        self.__client = client

        self.chat_window = tk.Tk()
        self.chat_window.title( f"Chat-Client - logged in as {self.__client.get_nickname()}")
        self.chat_message_var = tk.StringVar()  # bind variable for chat message
        # chat display ----
        # https://www.geeksforgeeks.org/python-tkinter-scrolledtext-widget/
        self.chat_area = st.ScrolledText(self.chat_window, state='disabled', width=80, height=20)
        self.chat_area.pack(padx=10, pady=10)
        # -------

        # input field for entering message and button to send it -----
        bottom_frame = tk.Frame(self.chat_window)
        bottom_frame.pack(padx=10, pady=10, fill=tk.X)
        # https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method

        self.chat_message = tk.Entry(bottom_frame, width=60, textvariable=self.chat_message_var)
        self.chat_message.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

        self.send_button = tk.Button(bottom_frame, text="Send", command=self.on_send)
        self.send_button.pack(side=tk.RIGHT)
        # -------


    def start_gui(self):
        """
        Starts the gui and let it run in a loop to wait and display incoming messages
        :return:
        """
        self.chat_window.mainloop()

    def display_message(self, message):
        """
        Displays an incoming message in the chat area
        :param message: The message to display
        :return:
        """
        # https://stackoverflow.com/questions/63055048/how-to-insert-text-to-scrolledtext-while-it-is-in-disabled-state-in-tkinter
        # https://gist.github.com/Yagisanatode/6ccef95e75c5686474c7
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END,message + "\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)  # scroll all the way down

    def on_send(self):
        """
        event method to activate once the send button is pressed
        It gets the message from the input field and sends it to the server
        clears the input field afterward
        :return:
        """
        message = self.chat_message_var.get().strip()
        if message:
            #timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            #full_message = f"{timestamp}  {self.__client.get_nickname()}: {message}"
            #self.__client.send_message(full_message)
            self.__client.send_message(message)
            # https://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter
            self.chat_message.delete(0, tk.END)