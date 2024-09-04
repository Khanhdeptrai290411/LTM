import socket
from datetime import datetime
HOST="127.0.0.1"
SERVER_PORT = 65431
FORMAT="utf8"

LOGIN ="login"
SIGNUP= "signup"
def sendList(client,list):
    for item in list:
        client.sendall(item.encode(FORMAT))
        client.recv(1024)   
    msg = "end"
    client.send(msg.encode(FORMAT)) 

def LoginClient(client):
    user_info=[]
    name= input("Name: ")
    user_info.append(name)
    email = input("Email: ")
    user_info.append(email)
    Passwd= input("password: ")
    user_info.append(Passwd)

    sendList(client,user_info)
            
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)


try:
    client.connect((HOST,SERVER_PORT))

    print("CLIENT ADDRESS ",client.getsockname())
    msg = None
    while(msg!="x"):
        msg = input("Type: ")
        client.sendall(msg.encode(FORMAT))
        if(msg==SIGNUP):
            LoginClient(client)
            client.recv(1024)
        
            
except:
 print("Error")
 

client.close()