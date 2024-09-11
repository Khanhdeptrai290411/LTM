import socket
import threading
import mysql.connector
from datetime import datetime
import bcrypt


HOST = '127.0.0.1'
PORT = 65435
FORMAT = 'utf-8'
MAX_CONNECTIONS = 50
OK = 'ok'
LOGIN='login'
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

def Recv(conn):
    lst = []
    item = conn.recv(1024).decode(FORMAT)
    while item != "end":  
        lst.append(item)
        conn.sendall(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)
    return lst

def checkLogin(conn,lst):
    print('Login start')
    try:
        # mail = conn.recv(1024).decode(FORMAT)  # Receive email
        # conn.sendall(mail.encode(FORMAT))  # Send back 'mail' to confirm receipt

        # paswd = conn.recv(1024).decode(FORMAT)  # Receive password
        # conn.sendall(paswd.encode(FORMAT))  # Send back 'password' to confirm receipt
        
        cursor.execute('SELECT password_hash FROM User WHERE email = %s', (lst[0],))
        result = cursor.fetchall()  # Get a single result
        paswd= lst[1]
        msg = OK
        if result:
            data_password = result[0][0]  # Extract password hash from the database
            print(f"Password from DB: {data_password}")
            print(f"Password to compare: {paswd}")

            # Check password with bcrypt
            if bcrypt.checkpw(paswd.encode(FORMAT), data_password.encode('utf-8')):
                msg=OK
                print(msg)
                conn.sendall(msg.encode(FORMAT))
            else:
                msg=FAIL
                print(msg)
                conn.sendall(msg.encode(FORMAT))
        else:
            print('No matching user found')
            conn.sendall("User not found".encode(FORMAT))
    except mysql.connector.Error as err:
        print(f"Error: {err}")




    
def handle_client(conn, addr):
    try:
        print(f"Client connected: {addr}")
        while True:
            msg = conn.recv(1024).decode(FORMAT)
        # Xử lý thông điệp nhận được từ client
        
            if(msg==LOGIN):
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                lst = Recv(conn)
                print(lst)
                checkLogin(conn,lst)
            
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
