import socket
from datetime import datetime
import bcrypt
HOST="127.0.0.1"
SERVER_PORT = 65434
FORMAT="utf8"

LOGIN ="login"
SIGNUP= "signup"
def sendList(client,list):
    for item in list:
        client.sendall(item.encode(FORMAT))
        client.recv(1024)   
    msg = "end"
    client.send(msg.encode(FORMAT)) 

def SignUpClient(client):
    check=False
    while (check!=True):
        user_info = []
        name = input("Name: ")
        user_info.append(name)
        email = input("Email: ")
        user_info.append(email)
        Passwd = input("Password: ")
        salt = bcrypt.gensalt()
        Passwd2 = bcrypt.hashpw(Passwd.encode('utf-8'), salt).decode('utf-8')  # Chuyển đổi bytes sang string
        user_info.append(Passwd2)

        sendList(client, user_info)

        # Nhận phản hồi từ server
        sv = client.recv(1024).decode(FORMAT)
        if sv == "Signup successful.":
            
            print('SignUp successfully')
            check=True
        else:
            print(sv)  # In ra lỗi từ server và tiếp tục vòng lặp để nhập lại thông tin
    chat()
    
    
def chat():
    msg = None
    while(msg!="x"):
        msg = input("Type: ")
        client.sendall(msg.encode(FORMAT))
        client.recv(1024)
        if(msg==SIGNUP):
            SignUpClient(client)
            client.recv(1024)
        elif(msg==LOGIN):
            LogInClient(client)
            client.recv(1024)
        
        
def LogInClient(client):
    user_info=[]
    name= input("Name: ")
    user_info.append(name)
    email = input("Email: ")
    user_info.append(email)
    Passwd = input("Password: ")
    salt = bcrypt.gensalt()
    Passwd2 = bcrypt.hashpw(Passwd.encode('utf-8'), salt).decode('utf-8')  # Chuyển đổi bytes sang string
    user_info.append(Passwd2)

    sendList(client,user_info)
            
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)


try:
    client.connect((HOST,SERVER_PORT))
    chat()
    print("CLIENT ADDRESS ",client.getsockname())
   
            
except:
 print("Error")
 

client.close()