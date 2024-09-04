import socket
import threading
import mysql.connector
from datetime import datetime
import connectz

HOST = "127.0.0.1"
SERVER_PORT = 65434
FORMAT = "utf8"

#--------------------DB_connect_-------------------
if connectz.db_config.is_connected():
    print("Connected")
else:
    print("Not connected")

#------------------main--------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, SERVER_PORT))
s.listen()
LOGIN = "login"
SIGNUP = "signup"

# Flag to control server activity
server_active = True

def Recv(conn):
    lst = []
    item = conn.recv(1024).decode(FORMAT)
    while item != "end":  
        lst.append(item)
        conn.sendall(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)
    return lst


def serverSignup(cursor, db_conn, conn):
    created_at = datetime.now()
    status = True

    while True:  # Lặp lại cho đến khi đăng ký thành công
        # Nhận danh sách thông tin từ client
        lst = Recv(conn)
        print(lst, created_at, status)
        try:
            cursor.execute('INSERT INTO User(user_name, email, password_hash) VALUES (%s, %s, %s)', lst)
            db_conn.commit()
            # Nếu không có lỗi, gửi thông báo thành công và thoát khỏi vòng lặp
            conn.sendall("Signup successful.".encode(FORMAT))
            break
        except mysql.connector.errors.IntegrityError as err:
            print(f"Error: {err}")
            msg = "Error: Email already exists. Please signup again."
            conn.sendall(msg.encode(FORMAT))  # Gửi thông báo lỗi về client

        


def serverLogin(cursor, lst, db_conn):
    try: 
        cursor.execute('SELECT password_hash FROM User WHERE user_name = %s AND email = %s', (lst[0], lst[1]))
        password = cursor.fetchall()
        data_password = password[0]
        print(password)
        if(lst[2]== data_password):
            print('Login successfully')
        else:
            print('invalid password')
    except mysql.connector.Error as err:
        print(f"Error: {err}")


        


def handleClient(conn, addr):
    print("Client address ", conn.getsockname())

    db_conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='MeetingApp',
    )
    cursor = db_conn.cursor()

    msg = None
    while msg != "x" :

        msg = conn.recv(1024).decode(FORMAT)
        print("Client said ", msg)
        conn.sendall(msg.encode(FORMAT))
        if msg == SIGNUP:
            conn.sendall(msg.encode(FORMAT))
            serverSignup(cursor, db_conn, conn)
        elif msg == LOGIN:
            conn.sendall(msg.encode(FORMAT))
            lst = Recv(conn)
            serverLogin(cursor, lst, db_conn)

    print("Client ", addr, " finished, close ", conn.getsockname())
    cursor.close()
    db_conn.close()
    conn.close()


def stop_server():
    global server_active
    server_active = False
    s.close()  # Close the server socket to stop accepting new connections
    print("Server has been stopped.")

print("SERVER SIDE:")
print("Server ", HOST, SERVER_PORT)
print("Waiting for client")

try:
    while server_active:
        conn, addr = s.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.daemon = False
        thread.start()
except Exception as e:
    print(f"Server error: {e}")
s.close()
print("Server stopped")
