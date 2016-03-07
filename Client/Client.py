# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser

class Client:
    """
    This is the chat client class
    """
    host = "localhost"
    server_port = 9998

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """
        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.msg = MessageReceiver(self, self.connection)
        self.host = host
        self.server_port = server_port

        self.hasLoggedOn = False

        #msg is a request sent from the client to the server
        self.run()
        self.msg.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        print "Welcome to the chat! Type help to get help."

        while True:
            incoming = raw_input()

            if incoming == 'help':
                helpText = "Type login to log in. Type logout to log out. Type names to get all names."
                print helpText

            elif incoming == 'login' and not self.hasLoggedOn:
                print "Please type your desired username."

                incoming = raw_input()
                obj = {"request": "login", "content": incoming}
                try:
                    jsonobj = json.dumps(obj)
                except UnicodeDecodeError:
                    print "Invalid characters in username. Please try again."
                self.send_payload(jsonobj)
                self.hasLoggedOn = True

            elif incoming == 'logout' and self.hasLoggedOn:
                print "Logging out..."
                obj = {"request": "logout", "content": ""}
                try:
                    jsonobj = json.dumps(obj)
                    self.send_payload(jsonobj)
                    self.disconnect()
                    self.hasLoggedOn = False
                except UnicodeDecodeError:
                    print "Invalid characters"
                    continue

            elif incoming == 'logout' and not.self.hasLoggedOn:
                print "You have to be logged in to log out"

            elif incoming == 'names' and self.hasLoggedOn:
                obj = {"request": "names", "content": ""}
                try:
                    jsonobj = json.dumps(obj)
                except UnicodeDecodeError:
                    print "Invalid characters"
                self.send_payload(jsonobj)


    def disconnect(self):
        print "Disconnecting..."
        self.connection.close()
        self.hasLoggedOn = False
        print "You are disconnected."
        pass

    def receive_message(self, message):
        parser = MessageParser()
        parsedMessage = parser.parse()
        print parsedMessage
        pass

    def send_payload(self, data):
        self.connection.send(data)
        pass

        # More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
