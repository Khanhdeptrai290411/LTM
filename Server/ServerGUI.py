import socket

import threading
import time
import mysql.connector
from datetime import datetime
import bcrypt
 


HOST = '192.168.1.62'
PORT = 65432
FORMAT = 'utf-8'
MAX_CONNECTIONS = 50
OK = 'ok'
LOGIN='login'
SIGNUP='signup'
GET_CLIENTS='getclients'
FAIL='fail'
END='x'
LOGOUT='logout'
OPENCHATBOX='openchatbox'
CLICK_CHAT = 'click_chat'
# Thiết lập kết nối đến cơ sở dữ liệu
db_conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='MeetingApp',
)
cursor = db_conn.cursor()

# Tạo và cấu hình socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f'Server running on {HOST}:{PORT}')
print('Waiting for clients...')
Live_Account=[]
ID=[]
Ad=[]
User_info=[]
def send_Clients(conn, clients_list):
    print("send client start")
    # Send the list of clients
    data = "\n".join(clients_list) + "\nend"
    conn.sendall(data.encode(FORMAT))

        

def Recv(conn):
    lst = []
    item = conn.recv(1024).decode(FORMAT)
    while item != "end":  
        lst.append(item)
        conn.sendall(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)
    return lst


def sendList(conn, data_list):
    for item in data_list:
        # Convert each item to a string if it's not already
        item_str = ','.join(map(str, item))
        conn.sendall(item_str.encode(FORMAT))
        conn.recv(1024)  # Wait for acknowledgment
    msg = "end"
    conn.send(msg.encode(FORMAT))

        
def checkSignUp(conn, lst, addr):  # Thêm đối số addr
    print('Sign Start')
    try:
        created_at = datetime.now()
        status = True

        user_name = lst[0]
        email = lst[1]
        password_hash = lst[2]
        ip_address = addr[0]
        
        print(lst, addr, created_at, status)
        cursor.execute('INSERT INTO User(user_name, email, password_hash, ip_address) VALUES (%s, %s, %s, %s)', (user_name, email, password_hash, ip_address))
        db_conn.commit()
        conn.sendall(OK.encode(FORMAT))
        Ad.append(ip_address)
        ID.append(email)
        account=str(Ad[Ad.__len__()-1])+"-"+str(ID[ID.__len__()-1])
        Live_Account.append(account)
        print(Live_Account)
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        msg = "Error: Email already exists. Please signup again."
        print(msg)
        conn.sendall(FAIL.encode(FORMAT))
        
        
        
def checkLogin(conn, lst):
    print('Login start')
    print(f"Received list: {lst}")
    print(f"Current Ad list: {Ad}")
    print(f"Current ID list: {ID}")
    try:
        if len(lst) < 2:
            print(f"Error: Received list does not have enough elements: {lst}")
            conn.sendall(FAIL.encode(FORMAT))
            return
        
        cursor.execute('SELECT password_hash FROM User WHERE email = %s', (lst[0],))
        result = cursor.fetchall()
        paswd = lst[1]
        cursor.execute('SELECT * FROM User WHERE email = %s', (lst[0],))
        user_list = cursor.fetchall()
        msg = OK
        ip_address = addr[0]
        if result:
            data_password = result[0][0]
            if bcrypt.checkpw(paswd.encode(FORMAT), data_password.encode('utf-8')):
                msg = OK
                conn.sendall(msg.encode(FORMAT))
                
                Ad.append(ip_address)
                ID.append(lst[0])
                account = str(Ad[Ad.__len__()-1]) + "-" + str(ID[ID.__len__()-1])
                Live_Account.append(account)
                
                sendList(conn, user_list)
                print(Live_Account)
            else:
                msg = FAIL
                conn.sendall(msg.encode(FORMAT))
        else:
            conn.sendall("User not found".encode(FORMAT))
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    
def Remove_LiveAccount(conn):
    print('Logout start')
    try:
        # Nhận email từ client
        email = conn.recv(1024).decode(FORMAT)
        print(f"Received email for logout: {email}")

        # Tìm và xóa email trong Live_Account
        for row in Live_Account:
            parse = row.find("-")
            user_email = row[(parse + 1):]
            if user_email == email:
                ip_address = row[:parse]
                Ad.remove(ip_address)
                ID.remove(user_email)
                Live_Account.remove(row)
                conn.sendall("True".encode(FORMAT))
                return  # Exit after successful removal

        # Nếu không tìm thấy email
        conn.sendall("False".encode(FORMAT))
    except Exception as e:
        print(f"Error in Remove_LiveAccount: {e}")
        conn.sendall("False".encode(FORMAT))

    
def OpenChatBox(conn, addr, Live_Account, user_email):
    print('Open chat box')
    try:
        # Duyệt qua từng tài khoản trong Live_Account
        for account in Live_Account:
            # Phân tách thông tin tài khoản theo định dạng "ip_address-email"
            parse = account.find("-")
            if parse != -1:
                email = account[parse + 1:]
                
                # Bỏ qua email của người dùng hiện tại
                if email != user_email:
                    conn.sendall(email.encode(FORMAT))
                    # Đợi client xác nhận đã nhận email
                    conn.recv(1024)
        
        # Gửi thông báo kết thúc
        conn.sendall("end".encode(FORMAT))
    except Exception as e:
        print(f"Error: {e}")

def StartChat():
    asd
    
    
def handle_client(conn, addr):
    try:
        print(f"Client connected: {addr}")
        while True:
            msg = conn.recv(1024).decode(FORMAT)
            if msg == LOGIN:
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                lst = Recv(conn)
                print(lst)
                checkLogin(conn, lst)
            elif msg == SIGNUP:
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                lst = Recv(conn)
                print(lst)
                checkSignUp(conn, lst, addr)  # Truyền addr vào
            elif msg == GET_CLIENTS:
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                print(Live_Account)
                send_Clients(conn,Live_Account)
            elif msg == LOGOUT:
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                Remove_LiveAccount(conn)
            elif msg == OPENCHATBOX:
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                email = conn.recv(1024).decode(FORMAT)
                OpenChatBox(conn,addr,Live_Account,email)
            elif msg == CLICK_CHAT:
                print(msg)       
                conn.sendall(msg.encode(FORMAT))
                
    except Exception as e:
        print(f"Error handling client {addr}: {e}")

# Quản lý kết nối đồng thời
clients = []
check=True
try:
    while check:
        if len(clients) < MAX_CONNECTIONS:
            conn, addr = server_socket.accept()
            clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
        else:
            print("Max connections reached. Waiting for available slots...")
            check=False
            
            
except KeyboardInterrupt:
    print("Server stopped by user")
except Exception as e:
    print(f"Server error: {e}")
finally:
    for conn in clients:
        conn.close()
    server_socket.close()
    cursor.close()
    db_conn.close()
    print("Server resources cleaned up")
