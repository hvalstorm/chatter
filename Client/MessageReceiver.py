# -*- coding: utf-8 -*-
from threading import Thread

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and it allows
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """
        super(MessageReceiver, self).__init__() #Fjerner RuntimeError
        # Flag to run thread as a deamon
        self.daemon = True
        self.client = client
        self.connection = connection

    def run(self):
        while True:
            if self.client.hasLoggedOn:
                message = self.connection.recv(4096)

                if message:
                    self.client.receive_message(message)
