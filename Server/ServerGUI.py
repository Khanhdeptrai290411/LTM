import socket

import threading
import time
import mysql.connector
from datetime import datetime
import bcrypt
 
live_account_lock = threading.Lock()

HOST = '192.168.1.189'
PORT = 65434
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
SEND_MESSAGE='send_message'
UPDATE_ROOM='update_room'
CREATE_GROUP = 'create_group'
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
Groups=[]
ID=[]
Ad=[]
Conn=[]
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
        print(f"nhan duoc {item}")
        item = conn.recv(1024).decode(FORMAT)
    return lst

def sendListConn(conn, list):
    for item in list:
        print(f"Gửi {item} tới client {conn}")  # Log mỗi khi gửi item
        conn.sendall(item.encode(FORMAT))
        response = conn.recv(1024)  # Nhận phản hồi từ client
        print(f"Phản hồi từ client sau khi nhận {item}: {response.decode(FORMAT)}")
    msg = "end"

    conn.send(msg.encode(FORMAT))

        
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
        conn_add= str(conn)
        print(lst, addr, created_at, status)
        cursor.execute('INSERT INTO User(user_name, email, password_hash, ip_address) VALUES (%s, %s, %s, %s)', (user_name, email, password_hash, ip_address))
        db_conn.commit()
        cursor.execute('SELECT * FROM User WHERE email = %s', (lst[0],))
        user_list = cursor.fetchall()
        conn.sendall(OK.encode(FORMAT))
        sendList(conn, user_list)
        Ad.append(ip_address)
        ID.append(email)
        Conn.append(conn)
        account = {
        "ip_address": ip_address,
        "email": email,
        "conn_str": str(conn),  # Chuỗi biểu diễn để hiển thị
        "conn": conn  # Đối tượng socket để thao tác
        }
        Live_Account.append(account)
        print(Live_Account)
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        msg = "Error: Email already exists. Please signup again."
        print(msg)
        conn.sendall(FAIL.encode(FORMAT))
        
        
        
def checkLogin(conn, lst):
    print('Login start')

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
        conn_add= str(conn)
        if result:
            data_password = result[0][0]
            if bcrypt.checkpw(paswd.encode(FORMAT), data_password.encode('utf-8')):
                msg = OK
                conn.sendall(msg.encode(FORMAT))
                
                Ad.append(ip_address)
                ID.append(lst[0])
                Conn.append(conn)
                account = {
                "ip_address": ip_address,
                "email": lst[0],
                "conn_str": str(conn),  # Chuỗi biểu diễn để hiển thị
                "conn": conn  # Đối tượng socket để thao tác
                }
                Live_Account.append(account)
                
                sendList(conn, user_list)

                
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
        
        check_timra = False
        # Tìm và xóa email trong Live_Account
        for row in Live_Account:
            user_email = row['email']
            ip_address = row['ip_address']
            conn_user = row['conn_str']
            conn_address = row['conn']

            if user_email == email:
                # Xóa thông tin của người dùng
                Ad.remove(ip_address)
                ID.remove(user_email)
                Conn.remove(conn)
                Live_Account.remove(row)
                
                print(f"User with email {email} has disconnected.")
                print(Live_Account)
                conn.sendall("True".encode(FORMAT))
                conn.close()
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
        for email in ID:

            if email != user_email :
                print(email)       
                conn.sendall(email.encode(FORMAT))
                    # Đợi client xác nhận đã nhận email
                conn.recv(1024)
   
        
        # Gửi thông báo kết thúc
        conn.sendall("end".encode(FORMAT))
        conn.recv(1024)
    except Exception as e:
        print(f"Error: {e}")
        


def send_to_all():
    for conn in Conn:
        if conn:  # Kiểm tra xem kết nối có còn tồn tại không
            try:
                option = UPDATE_ROOM
                conn.sendall(option.encode(FORMAT))

                time.sleep(0.5)
            except Exception as e:
                print(f"Lỗi khi gửi lệnh tới {conn}: {e}")

    


def update_new_friendlist(conn, Live_Account):
    with live_account_lock:
        print('Update friend list bắt đầu')
        try:
            option = UPDATE_ROOM


            conn.sendall(option.encode(FORMAT))

            conn.recv(1024)  # Nhận xác nhận từ client
            for row in Live_Account:
                conn_user = row['conn']

                
                # Tạo danh sách bạn bè trừ chính client hiện tại
                friend_list = [user['email'] for user in Live_Account if user['conn'] != conn]
                # if user['conn'] != conn_user

                    
                # Gọi hàm sendListConn để gửi danh sách bạn bè
            sendListConn(conn, friend_list)
                    
        except Exception as e:
            print(f"Error: {e}")




        







        
        
# def send_message(msg, prefix="", destination=None, broadcast=False):
#     send_msg = bytes(prefix + msg, "utf-8")
#     if broadcast:
#         """Broadcasts a message to all the clients."""
#         for sock in clients:
#             sock.send(send_msg)
#     else:
#         if destination is not None:
#             destination.send(send_msg)
def CreateGroup(conn, friend_selected, group_name):
    try:
        created_at = datetime.now()
        insert_group_query = "INSERT INTO `Group` (group_name, created_time) VALUES (%s, %s)"
        cursor.execute(insert_group_query, (group_name,created_at))
        group_id = cursor.lastrowid  # Get the generated group ID

        # Step 2: Get user_id for each email in friend_selected
        for email in friend_selected:
            select_user_query = "SELECT user_id FROM User WHERE email = %s"
            cursor.execute(select_user_query, (email,))
            result = cursor.fetchone()
            if result:
                user_id = result[0]

                # Step 3: Insert into Participant table
                insert_participant_query = "INSERT INTO Participant (group_id, user_id) VALUES (%s, %s)"
                cursor.execute(insert_participant_query, (group_id, user_id))
            else:
                print(f"Email {email} not found in the User table")

        # Commit the transaction
        db_conn.commit()
        # Thêm logic xử lý tạo nhóm
        print('Friend: ', friend_selected, 'Group name: ', group_name)
        # Phản hồi lại client rằng việc tạo nhóm đã thành công
        conn.sendall("GROUP_CREATED_SUCCESS".encode(FORMAT))
    except Exception as e:
        print(f"Error: {e}")
        conn.sendall(f"Error: {e}".encode(FORMAT))




   
def handle_client(conn, addr):
    try:
        print(f"Client connected: {addr}")
        while True:
            msg = conn.recv(1024).decode(FORMAT)
            print(f'hien tai dang o handle_client {conn}')
            if msg == LOGIN:
                print(msg)
                conn.sendall(msg.encode(FORMAT)) #gui lan 1 cho handle lenh LOGIN
                conn.recv(1024) #nhan tiep lenh LOGIN tu ham
                conn.sendall(msg.encode(FORMAT)) # tra lai phan hoi cho ham
                lst = Recv(conn)
                print(lst)
                checkLogin(conn, lst)
                print("Toi ham send to all")
                send_to_all()
            elif msg == SIGNUP:
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                conn.recv(1024)
                conn.sendall(msg.encode(FORMAT))
                lst = Recv(conn)
                print(lst)
                checkSignUp(conn, lst, addr)  # Truyền addr vào
                print("Toi ham send to all")
                send_to_all()
            elif msg == GET_CLIENTS:
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                print(Live_Account)
                send_Clients(conn,Live_Account)
            elif msg == LOGOUT:
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                conn.recv(1024)
                conn.sendall(msg.encode(FORMAT))
                Remove_LiveAccount(conn)
                print("Toi ham send to all")
                send_to_all()
            elif msg == OPENCHATBOX:
                print(msg)
                conn.sendall(msg.encode(FORMAT))
                conn.recv(1024)
                conn.sendall(msg.encode(FORMAT))
                email = conn.recv(1024).decode(FORMAT)
                OpenChatBox(conn,addr,Live_Account,email)
            elif msg == UPDATE_ROOM:
                update_new_friendlist(conn,Live_Account)
            # elif msg == SEND_MESSAGE:
            elif msg == CREATE_GROUP:
                print(f'nhan lenh {msg} tu client')
                conn.sendall(msg.encode(FORMAT))
                conn.recv(1024)
                conn.sendall(msg.encode(FORMAT))
                friend_selected = Recv(conn)
                print(f"Selected friends: {friend_selected}")
                conn.sendall(msg.encode(FORMAT))
                group_name = conn.recv(1024).decode(FORMAT)
                print(f"Group name: {group_name}")
                CreateGroup(conn,friend_selected,group_name)
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