import socket
import threading
import time
import mysql.connector
from datetime import datetime
import bcrypt
 


HOST = '192.168.110.162'
PORT = 65433
FORMAT = 'utf-8'
MAX_CONNECTIONS = 50
OK = 'ok'
LOGIN='login'
SIGNUP='signup'
GET_CLIENTS='getclients'
FAIL='fail'
END='x'

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
                print(Live_Account)
            else:
                msg = FAIL
                conn.sendall(msg.encode(FORMAT))
        else:
            conn.sendall("User not found".encode(FORMAT))
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# def send_live_accounts_to_gui():
#     # Gửi dữ liệu Live_Account đến client GUI qua một socket khác hoặc một cách tương tự
#     gui_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     gui_socket.connect(('localhost', PORT_GUI))  # Địa chỉ và cổng của GUI
#     while True:
#         data = ' '.join(Live_Account)
#         gui_socket.sendall(data.encode(FORMAT))
#         time.sleep(5)  # Cập nhật mỗi 5 giây
#     gui_socket.close()

# # Chạy một thread riêng để gửi dữ liệu
# threading.Thread(target=send_live_accounts_to_gui).start()        
   
        
        
    
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
