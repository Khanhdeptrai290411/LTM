import threading
import time
from customtkinter import *
import tkinter
from PIL import Image  # Import PIL để mở hình ảnh
import socket
import SignupPage
import LoginPage
import EntryPage
import HomePage
import Document_frame
import NewGroup
import main_UI
from vidstream import *



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⠤⠒⠒⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀  ⢀⡯⠴⠶⠶⠒⠢⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀  ⡎⡤⠖⠂⡀⠒⡢⡌⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠯⢭⣵⠑⣯⡭⢹⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⢠⣤⠄⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⢄⣈⣟⢁⢴⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣀⢴⠒⡝⠁⠬⠛⣚⡩⠔⠉⢻⠒⣦⢄⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢀⢎⠁⡌⢰⠁⠀⠀⠀⠀⠀⠀⠀⢸⠀⡛⠀⡷⡀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⣀⣾⣷⣠⠃⢸⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⢹⢰⠁⢳⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢸⡿⠟⢿⢳⡏⠀⠀⠀⠀⠀⠀⠀⢠⡟⣶⣘⢞⡀⠘⡆⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⡼⢺⣯⢹⢰⡏⠒⠒⠒⠊⠀⠐⢒⣾⣹⣸⢹⣾⡇⠀⢣⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⣏⣾⠃⠀⣼⡟⣢⣀⡠⠤⣀⡰⢋⡝⣱⣹⠇⣿⣧⣴⠸⡄⠀⠀⠀⠀
# ⠀⠀⠀⠀⡏⡞⡆⢠⡇⣟⠭⡒⠭⠭⠤⠒⣡⠔⣽⡇⣂⣿⠟⠃⢀⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢧⡇⡧⢫⠃⣷⣽⣒⣍⣉⣈⡩⢴⠾⡳⢡⢸⣛⣪⡗⢴⠁⠀⠀⠀⠀
# ⠀⠀⠀⠀⣼⢃⠷⣸⣤⣯⢞⡥⢍⣐⣂⠨⠅⠊⡠⢃⣟⢏⠹⣎⣆⡀⠀⠀⠀⠀
# ⠀⡠⠶⠚⠛⠛⠽⢹⡟⡖⢓⠿⣝⠓⠒⠒⠒⠭⢤⠗⣯⣩⣽⣿⠷⣾⣿⢷⣆⠀
# ⠜⣌⠢⢄⣀⡀⠀⡞⢡⠘⢄⠑⠨⢉⣀⠉⣀⠄⢊⠜⡸⠛⣿⡍⠉⠉⠈⢁⠁⠇
# ⠈⢯⡓⠦⠤⠬⠭⣵⠀⠱⢄⠑⠲⠤⠤⠤⠤⠒⢁⡔⠁⢠⣏⣡⣤⣤⡶⠜⣻⠃
# ⠀⠈⠙⠛⠒⠛⠻⠯⠕⠤⣀⣉⣓⣒⣂⣒⣒⣊⣁⣠⠔⠛⠂⠒⠛⠓⠛⠚⠉⠀





import bcrypt
import pickle
HOST = "192.168.1.189"
SERVER_PORT = 65439
FORMAT = "utf8"
OK = 'ok'
LOGIN='login'
SIGNUP='signup'
FAIL='fail'
END='x'
LOGOUT='logout' 
OPENCHATBOX='openchatbox'
SEND_MESSAGE='send_message'
UPDATE_ROOM='update_room'
CREATE_GROUP = 'create_group'
KICK_USER = 'kick_user'
CALLVIDEO='call_video'
REQUESTCALL='request_call'
class App(CTk):
    
    def __init__(self):
        super().__init__()
        self.geometry("900x500+300+200+700")
        set_appearance_mode("light")  # Bạn có thể chuyển thành "dark" để thử nghiệm
        
        self.User_info=[]
        self.user_info=[]
        self.Friend_list=[]
        self.friend_to_call=None
        self.title('C')
        self.video_server = None  # Thêm thuộc tính video_server để lưu server
        self.server_thread = None  # Thêm thuộc tính server_thread để lưu luồng server
        self.local_ip_address=None
        #--------components----------------
        container = CTkFrame(self)  # Đảm bảo container có master
        container.pack(fill="both", expand=True)
        
        # Dictionary to hold frames
        self.frames = {}
        
        for F in (SignupPage.SignUp, LoginPage.LogIn,HomePage.Home,main_UI.Main_Screen):  # Sử dụng các lớp, không phải module
            frame = F(container, self)  # Tạo một frame từ lớp đã nhập
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[F] = frame
        
        # Hiển thị frame đầu tiên (EntryPage)
        self.show_frame(LoginPage.LogIn)
    
    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

        if page_class == main_UI.Main_Screen:
            # Điều chỉnh kích thước của cửa sổ
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            window_width = int(screen_width * 0.99)  # Ví dụ: 80% chiều rộng màn hình
            window_height = int(screen_height * 0.99)  # Ví dụ: 80% chiều cao màn hình
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        else:
            # Đặt lại kích thước khi quay lại các frame khác
            self.geometry("900x500+300+200")
            
            
            
 
    
    
    
    
    def sendList(self,client, list):
        for item in list:
            client.sendall(item.encode(FORMAT))
            print('list co item: ',item)
            client.recv(1024)
        msg = "end"
        client.send(msg.encode(FORMAT))
    def Recv(self,client):
        lst = []
        item = client.recv(1024).decode(FORMAT)
        print(f"Nhận dữ liệu từ server: {item}")
        while item != "end":  
            lst.append(item)
            client.sendall(item.encode(FORMAT))
            item = client.recv(1024).decode(FORMAT)
            print(f"Nhận thêm dữ liệu từ server: {item}")
        return lst
    
    
    def User_info_Recv(self,client):
        lst = []
        item = client.recv(1024).decode(FORMAT)
        while item != "end":  
            lst.append(item)
            client.sendall(item.encode(FORMAT))
            item = client.recv(1024).decode(FORMAT)
        return lst
    
    
    
    def SignUp(self):
        self.connect_to_server()
        option = SIGNUP
        client.sendall(option.encode(FORMAT))
        
        
    def SignUpUser(self, curFrame):
        user_info = []
        try:
            option = SIGNUP
            client.sendall(option.encode(FORMAT))
        # Nhập thông tin người dùng
            user_name = curFrame.text_user_name.get()
            user_email = curFrame.text_email.get()
            user_password = curFrame.text_password.get()

        # Kiểm tra trường hợp trống
            if user_email == "Email" or user_name == "User Name" or user_password == "Password":
                curFrame.label_notice.configure(text="Fields cannot be empty")
                return

        # Tạo hash password
            salt = bcrypt.gensalt()
            Passwd2 = bcrypt.hashpw(user_password.encode('utf-8'), salt).decode('utf-8')

        # In thông tin
            print(f"Email: {user_email}, Password: {user_password}, userName: {user_name}")

        # Gửi SIGNUP yêu cầu đến server


        # Gửi thông tin người dùng sau khi server đã phản hồi
            if client.recv(1024).decode(FORMAT) == SIGNUP:
                user_info.append(user_name)
                user_info.append(user_email)
                user_info.append(Passwd2)
                self.sendList(client, user_info)

            # Nhận thông báo từ server
                response = client.recv(1024).decode(FORMAT)
                if response == FAIL:
                    curFrame.label_notice.configure(text="Email already exists. Please signup again")
                else:
                    lst = self.User_info_Recv(client)
                    self.User_info = lst
                    fields = self.User_info[0].split(',')
                    self.user_info = {
                        'user_id': fields[0],
                        'user_name': fields[1],
                        'email': fields[2],
                        'password_hash': fields[3],
                        'ip_address': fields[4],
                        'status': fields[5],
                        'created_at': fields[6]
                    }
                    self.serverToCall()
                    self.show_frame(main_UI.Main_Screen)
        except Exception as e:
            print('Error: Server is not responding', str(e))
    
             
    def LogIn(self):
        self.connect_to_server()
        option = LOGIN
        client.sendall(option.encode(FORMAT)) # gui lan 1
              
              
    def LogInUser(self, curFrame):
        user_info = []   

        try:
            option = LOGIN
            client.sendall(option.encode(FORMAT)) # gui lan 2
            user_email = curFrame.text_email.get()
            password = curFrame.text_password.get()
            if user_email == "Email" or password == "Password":
                curFrame.label_notice.configure(text="Fields cannot be empty")
                return
        
            print(f"Email: {user_email}, Password: {password}")  # In ra thông tin
        
            
            uu=client.recv(1024).decode(FORMAT)#nhan phan hoi rang da nhan lenh login tu server
            print(uu)
            
            user_info.append(user_email)
            user_info.append(password)
            
            # client.sendall(user_email.encode(FORMAT))

            # client.sendall(password.encode(FORMAT))
            self.sendList(client, user_info)
            
            response = client.recv(1024).decode(FORMAT)# nhan thong bao thanh cong hoac ko tu server
            # if(user_email=='admin'):
            #     if(response=="User not found"):
            #         curFrame.label_notice.configure(text="User not found")
            #         return
            #     elif(response==FAIL):
            #         curFrame.label_notice.configure(text="Invalid Password")
            #         return
            #     else:
            #         self.show_frame(ServerPage)
            # else:
            if(response=="User not found"):
                curFrame.label_notice.configure(text="User not found")
                return
            elif(response==FAIL):
                curFrame.label_notice.configure(text="Invalid Password")
                return
            else:
                lst = self.User_info_Recv(client)
                self.User_info = lst
                fields = self.User_info[0].split(',')
                self.user_info = {
                    'user_id': fields[0],
                    'user_name': fields[1],
                    'email': fields[2],
                    'password_hash': fields[3],
                    'ip_address': fields[4],
                    'status': fields[5],
                    'created_at': fields[6]
                }
                print(self.user_info['user_name'])
                self.serverToCall()
                self.show_frame(main_UI.Main_Screen)
                self.title(self.user_info.get('email') if self.user_info else 'C')
                print("da chay xong loginuser")
         
        except Exception as e:
            print('Error: Server is not responding', str(e))
    
    # def TestFrame(self):
    # show_frame(main_UI.Main_Screen)

    def Logout(self):
        option = LOGOUT
        client.sendall(option.encode(FORMAT))
        
    def LogoutUser(self):
        try:
            option = LOGOUT
            client.sendall(option.encode(FORMAT))
            client.recv(1024).decode(FORMAT)
            # Gửi email của người dùng đến server
            email = self.user_info['email']
            client.sendall(email.encode(FORMAT))
            
            # Nhận phản hồi từ server
            response = client.recv(1024).decode(FORMAT)
            print(response)
            if response == "True":
                self.show_frame(LoginPage.LogIn)
                self.stopServer()
                client.close()
                print('disconnected from server')
            else:
                print("Logout failed.")
        except Exception as e:
            print('Error: Server is not responding', str(e))
    # def sendMessage(self):
    #     option = SEND_MESSAGE
    #     client.sendall(option.encode(FORMAT))
        
    # def sendMessageUser(self,currentFrame):
    #     try:
    #         option = SEND_MESSAGE
    #         client.sendall(option.encode(FORMAT))
    #         client.recv(1024)
    #         message = currentFrame.message_entry.get()
    #         client.sendall(message.encode(FORMAT))
            
    #         return message
    #     except Exception as e:
    #         print('no message', str(e))

    def createGroup(self):
        option = CREATE_GROUP
        print(f'gui yeu cau {option} den Server')
        client.sendall(option.encode(FORMAT))
        
    def createGroupUser(self, curFrame):
        friend_selected=[]
        try:
            option = CREATE_GROUP
            client.sendall(option.encode(FORMAT))  # Bước 1: Gửi yêu cầu tạo nhóm
            print(f'gui lenh {option} them lan nua')
            client.recv(1024)  # Nhận phản hồi từ server
            print('nhan response')
            # Bước 2: Gửi danh sách bạn bè được chọn
            friend_selected = curFrame.selected_friends
            email = self.user_info['email']
            friend_selected.append(email)
            
            
            # friend_selected = listUser
            
            self.sendList(client, friend_selected)
            print(f'gui list {friend_selected}')
            client.recv(1024)  # Nhận phản hồi từ server
            print('nhan respone lan 2')
            # Bước 3: Gửi tên nhóm
            group_name = curFrame.group_name
            # group_name=groupname
            client.sendall(group_name.encode(FORMAT))
            print(f'gui ten group {group_name}')
            print('List bạn bè đã chọn:', friend_selected, 'Tên nhóm:', group_name)

            # Bước 4: Nhận phản hồi từ server về việc tạo nhóm
            response = client.recv(1024).decode(FORMAT)
            if response == "GROUP_CREATED_SUCCESS":
                print("Nhóm đã được tạo thành công!")
            else:
                print("Lỗi khi tạo nhóm:", response)
        except Exception as e:
            print('Error: Server is not responding', str(e))

    def CallVideo(self,friend):
        option = CALLVIDEO
        self.friend_to_call=friend
        client.sendall(option.encode(FORMAT))
    def CallVideoUser(self):
        option = CALLVIDEO
        client.sendall(option.encode(FORMAT))
        client.recv(1024)
        friend = self.friend_to_call
        print(friend, ' day la email cua ban call')
        client.sendall(friend.encode(FORMAT))
        client.recv(1024)
        email = self.user_info['email']
        print(email,' day la email cua minh')
        client.sendall(email.encode(FORMAT))
        client.recv(1024)
        print('day la dia chi ip ',self.local_ip_address)
        client.sendall(self.local_ip_address.encode(FORMAT))
    
    
    
    
    def handleClient(self):
        while self.connected:
            print(f'dang o {client} ')
            data = client.recv(1024).decode(FORMAT) # nhan lan 1 cua handle ben server
            print(data,'7749')
            if data:
                if data == LOGOUT:
                    self.LogoutUser()
                elif data == UPDATE_ROOM:

                    client.send(data.encode(FORMAT)) #gui toi handle ben kia

                    client.recv(1024)

                    client.send(data.encode(FORMAT))

                    lst = self.Recv(client)

                    self.Update_Room(lst)
                
                   
                elif data == LOGIN:
                    self.LogInUser(self.frames[LoginPage.LogIn])
                    
                elif data == SIGNUP:
                    self.SignUpUser(self.frames[SignupPage.SignUp])
                    
                elif data == OPENCHATBOX:
                    self.OpenChatBoxUser()
                elif data == CREATE_GROUP:
                    print(f'nhan lenh {data} tu Server')
                    self.createGroupUser(self.frames[main_UI.Main_Screen].frames[NewGroup.CreateGroup_frame])
                elif data == KICK_USER:
                    self.show_frame(LoginPage.LogIn)
                    client.close()
                elif data == CALLVIDEO:
                    self.CallVideoUser()
                elif data == REQUESTCALL:
                    print(f'nhan lenh {data} tu admin')
                    data_recv=client.recv(1024)
                    data_loads=pickle.loads(data_recv)
                    friend=data_loads[0]
                    my_email=data_loads[1]
                    ip=data_loads[2]
                    print(data_loads[0])
                    self.show_call_notification(friend, my_email, ip)
                    # client.sendall(data.encode(FORMAT))
                    # print('phan hoi den admin')
                    
                    # client.recv(1024)
                    
                    # client.sendall(friend.encode(FORMAT))
                    # client.recv(1024)
                    
                    # client.sendall(my_email.encode(FORMAT))
                    # client.recv(1024)
                    
                    # client.sendall(ip.encode(FORMAT))
                    # client.recv(1024)
                    
                    # print('nhan phan hoi tu ham request')
                    # client.sendall(data.encode(FORMAT))
                    # print('phan hoi den ham request')
                    # client.recv
 # Giảm tải chu kỳ của thread

    
    
    def OpenChatBox(self):
        option = OPENCHATBOX
        client.sendall(option.encode(FORMAT))
    def OpenChatBoxUser(self):
        try:
            option = OPENCHATBOX
            client.sendall(option.encode(FORMAT))
            client.recv(1024)  # Chờ phản hồi từ server

            email = self.user_info['email']
            client.sendall(email.encode(FORMAT))

            response = self.Recv(client)  # Nhận phản hồi từ server 
            print("Dữ liệu nhận được từ server:", response)

            # Lọc bỏ email của người dùng hiện tại
            self.Friend_list = [friend for friend in response if friend != email]

            # Cập nhật giao diện với danh sách bạn bè mới
            self.update_main_screen()
            
        except Exception as e:
            print('Error: Server is not responding', str(e))       
            return []
    # def Update_Room(self):
    #     try:
    #         response = self.Recv(client)  # Nhận phản hồi từ server 
    #         print("Dữ liệu nhận được từ server:", response)

    #         self.Friend_list = response
    #         print(self.Friend_list)

    #         self.update_main_screen()
    #     except Exception as e:
    #         print('Error: Server is not responding', str(e))       
    #         return []
    def Update_Room(self,lst):
        try:
            # Gọi hàm Recv để nhận danh sách bạn bè từ server
            self.Friend_list = lst


            print("Danh sách bạn bè cập nhật:", self.Friend_list)
            self.update_main_screen()  # Cập nhật lại giao diện với danh sách mới
  

        except Exception as e:
            print('Error: Server is not responding', str(e))
            return []



    def update_main_screen(self):
        # Cập nhật Main_Screen với Friend_list mới
        if hasattr(self, 'frames') and main_UI.Main_Screen in self.frames:
            main_screen = self.frames[main_UI.Main_Screen]
            main_screen.update_friend_list(self.Friend_list)   
    

            
    def connect_to_server(self):
        global client  # Đảm bảo bạn sử dụng client toàn cục
        try:
            # Tạo một socket mới trước mỗi lần kết nối
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST, SERVER_PORT))
            self.connected = True  # Đặt trạng thái kết nối là True khi kết nối thành công
            print("Client connected successfully!")
            self.rT = threading.Thread(target=self.handleClient)
            self.rT.start()
        except Exception as e:
            self.connected = False  # Đặt trạng thái kết nối là False nếu xảy ra lỗi
            print(f"Failed to connect: {str(e)}")
            
            
            
            
    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Kết nối tới máy chủ DNS của Google để lấy IP cục bộ
            s.connect(("8.8.8.8", 80))
            ip_address = s.getsockname()[0]
        except Exception:
            # Nếu không thể lấy IP cục bộ, sử dụng localhost
            ip_address = "127.0.0.1"
        finally:
            s.close()
        return ip_address
    def serverToCall(self):
        # Tạo server lắng nghe video
        local_ip_address = self.get_local_ip()
        self.local_ip_address = local_ip_address
        self.video_server = StreamingServer(local_ip_address, 33333)  # Dùng IP cục bộ và cổng 12345

        # Chạy server trên luồng riêng để không chặn giao diện
        self.server_thread = threading.Thread(target=self.video_server.start_server)
        self.server_thread.start()

        print(f"Video server is running at {local_ip_address}:12345")
        
    def stopServer(self):
        if self.video_server:
            self.video_server.stop_server()  # Dừng server nếu nó đang chạy
            print("Video server has been stopped.")
            self.video_server = None  # Xóa tham chiếu tới server để tránh sử dụng lại
        if self.server_thread:
            self.server_thread.join()  # Đợi luồng server dừng hẳn
            self.server_thread = None
    def show_call_notification(self, friend, my_email, ip):
    # Tạo một cửa sổ Toplevel (pop-up)
        popup = CTkToplevel(self)
        popup.title("Incoming Call")

        # Đặt kích thước cửa sổ
        popup.geometry("300x200")

        # Hiển thị thông tin về cuộc gọi
        label = CTkLabel(popup, text=f"{friend} is calling from {ip}.\nYour email: {my_email}")
        label.pack(pady=20)

        # Nút Accept Call
        accept_button = CTkButton(popup, text="Accept", command=lambda: self.accept_call(popup, ip))
        accept_button.pack(side="left", padx=20, pady=10)

        # Nút Decline Call
        decline_button = CTkButton(popup, text="Decline", command=popup.destroy)
        decline_button.pack(side="right", padx=20, pady=10)


    def accept_call(self, popup, target_ip):
        print(f"Call Accepted! Streaming to {target_ip}")
        popup.destroy()  # Đóng cửa sổ thông báo

        # Bắt đầu cuộc gọi video
        self.start_camera_stream(target_ip)

        # Hiển thị giao diện cuộc họp với nút End Call
        self.show_in_meeting_interface()

    def start_camera_stream(self, target_ip):
        self.camera_client = CameraClient(target_ip, 33333)  # Lưu đối tượng camera_client
        self.camera_thread = threading.Thread(target=self.camera_client.start_stream)
        self.camera_thread.start()
        print(f"Streaming video to {target_ip}")

               
    def stop_camera_stream(self):
        if self.camera_client:
            self.camera_client.stop_stream()  # Dừng việc truyền phát video
            self.camera_client = None
            print("Camera stream stopped.")

    def end_call(self, meeting_popup):
    # Đóng cửa sổ cuộc họp
        meeting_popup.destroy()
        
        # Dừng camera stream
        self.stop_camera_stream()
        
        # Gửi thông báo kết thúc cuộc gọi đến server nếu cần
        if self.connected:
            client.sendall("END_CALL".encode(FORMAT))
        
        print("Call has ended.")
    def show_in_meeting_interface(self):
    # Tạo cửa sổ Toplevel mới cho giao diện cuộc họp
        meeting_popup = CTkToplevel(self)
        meeting_popup.title("In Call")

        # Thiết lập kích thước cửa sổ cuộc họp
        meeting_popup.geometry("400x300")

        # Nút ngắt cuộc gọi
        end_call_button = CTkButton(meeting_popup, text="End Call", command=lambda: self.end_call(meeting_popup))
        end_call_button.pack(pady=20)

        return meeting_popup


# Tạo và chạy ứng dụng
home = App()
# home.connect_to_server()
home.mainloop()