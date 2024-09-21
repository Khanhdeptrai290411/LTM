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

import main_UI



import bcrypt
HOST = "192.168.1.102"
SERVER_PORT = 65435
FORMAT = "utf8"
OK = 'ok'
LOGIN='login'
SIGNUP='signup'
FAIL='fail'
END='x'
LOGOUT='logout' 
OPENCHATBOX='openchatbox'

UPDATE_ROOM='update_room'
class App(CTk):
    
    def __init__(self):
        super().__init__()
        self.geometry("900x500+300+200+700")
        set_appearance_mode("light")  # Bạn có thể chuyển thành "dark" để thử nghiệm
        
        self.User_info=[]
        self.user_info=[]
        self.Friend_list=[]
        self.title('C')

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
            window_width = int(screen_width * 0.8)  # Ví dụ: 80% chiều rộng màn hình
            window_height = int(screen_height * 0.8)  # Ví dụ: 80% chiều cao màn hình
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        else:
            # Đặt lại kích thước khi quay lại các frame khác
            self.geometry("900x500+300+200")
            
            
            
 
    
    
    
    
    def sendList(self,client, list):
        for item in list:
            client.sendall(item.encode(FORMAT))
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
                
                client.close()
                print('disconnected from server')
            else:
                print("Logout failed.")
        except Exception as e:
            print('Error: Server is not responding', str(e))

    def handleClient(self):
        while self.connected:
            data = client.recv(1024).decode(FORMAT) # nhan lan 1 cua handle ben server
            if data:
                if data == LOGOUT:
                    self.LogoutUser()
                elif data == UPDATE_ROOM:
                    print(f"Client {client} đã nhận lệnh UPDATE_ROOM, gửi xác nhận lại")
                    client.send(data.encode(FORMAT)) #gui toi handle ben kia
                    print(f"Client {client} đã gửi xác nhận lệnh UPDATE_ROOM")
                    client.recv(1024)
                    print(f"Client {client} đã nhận phản hồi từ server")
                    client.send(data.encode(FORMAT))
                    print(f"Client {client} đã gửi lại lệnh xác nhận UPDATE_ROOM")
                    lst = self.Recv(client)
                    print(f"Client {client} đã nhận danh sách bạn bè: {lst}")
                    self.Update_Room(lst)
                
                   
                elif data == LOGIN:
                    self.LogInUser(self.frames[LoginPage.LogIn])
                elif data == SIGNUP:
                    self.SignUpUser(self.frames[SignupPage.SignUp])
                elif data == OPENCHATBOX:
                    self.OpenChatBoxUser()
                 
                
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

            # Kiểm tra xem danh sách bạn bè có hợp lệ không
            if self.Friend_list:
                print("Danh sách bạn bè cập nhật:", self.Friend_list)
                self.update_main_screen()  # Cập nhật lại giao diện với danh sách mới
            else:
                print("Không có bạn bè nào trong danh sách.")

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
            rT = threading.Thread(target=self.handleClient)
            rT.start()
        except Exception as e:
            self.connected = False  # Đặt trạng thái kết nối là False nếu xảy ra lỗi
            print(f"Failed to connect: {str(e)}")


            
               



# Tạo và chạy ứng dụng
home = App()
# home.connect_to_server()
home.mainloop()