import threading
import socket
import argparse
import os

class Server(threading.Thread):
        def __init__(self,host,port):
                super().__init__()
                self.connections=[]
                self.host = host
                self.port = port

        def run(self):
                socket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
                socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEDDR, 1)
                socket.bind((self.host, self.port))

                socket.listen(1)
                print("Listennig at ",sock.getsockname())