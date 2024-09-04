import socket
from datetime import datetime
import bcrypt

HOST = "127.0.0.1"
SERVER_PORT = 65435
FORMAT = "utf8"

LOGIN = "login"
SIGNUP = "signup"

def sendList(client, list):
    for item in list:
        client.sendall(item.encode(FORMAT))
        client.recv(1024)
    msg = "end"
    client.send(msg.encode(FORMAT))

def SignUpClient(client):
    check = False
    while check != True:
        user_info = []
        name = input("Name (or 'x' to cancel): ")  # Thêm hướng dẫn nhập 'x' để thoát
        if name == 'x':  # Kiểm tra nếu người dùng nhập 'x' để quay lại chat
            chat(client)
            return
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
            check = True
        else:
            print(sv)  # In ra lỗi từ server và tiếp tục vòng lặp để nhập lại thông tin
    
    chat(client)

def LogInClient(client):
    check = False
    while check != True:
        user_info = []
        name = input("Name (or 'x' to cancel): ")  # Thêm hướng dẫn nhập 'x' để thoát
        if name == 'x':  # Kiểm tra nếu người dùng nhập 'x' để quay lại chat
            chat(client)
            return
        user_info.append(name)
        
        email = input("Email: ")
        user_info.append(email)
        
        Passwd = input("Password: ")
        user_info.append(Passwd)  # Gửi mật khẩu plain text

        sendList(client, user_info)
        sv = client.recv(1024).decode(FORMAT)
        if sv == "Login successfully":
            print('Login successfully')
            check = True
        else:
            print(sv)  # In ra lỗi từ server và tiếp tục vòng lặp để nhập lại thông tin
    
    chat(client)

def chat(client):
    msg = None
    while msg != "x":
        msg = input("Type your message (or 'x' to exit): ")
        client.sendall(msg.encode(FORMAT))
        client.recv(1024)
        if msg == SIGNUP:
            SignUpClient(client)
        elif msg == LOGIN:
            LogInClient(client)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, SERVER_PORT))
    chat(client)
    print("CLIENT ADDRESS ", client.getsockname())
except Exception as e:
    print(f"Error: {e}")

client.close()
