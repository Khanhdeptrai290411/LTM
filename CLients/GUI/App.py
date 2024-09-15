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
HOST = "172.16.2.151"
SERVER_PORT = 65432
FORMAT = "utf8"
OK = 'ok'
LOGIN='login'
SIGNUP='signup'
FAIL='fail'
END='x'
LOGOUT='logout'
OPENCHATBOX='openchatbox'
CLICK_CHAT = 'click_chat'
class App(CTk):
    
    def __init__(self):
        super().__init__()
        self.geometry("900x500+300+200+700")
        set_appearance_mode("light")  # Bạn có thể chuyển thành "dark" để thử nghiệm
        self.title("C")
        self.User_info=[]
        self.user_info=[]
        self.Friend_list=['ad']
        
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
        while item != "end":  
            lst.append(item)
            client.sendall(item.encode(FORMAT))
            item = client.recv(1024).decode(FORMAT)
        return lst
    
    
    def User_info_Recv(self,client):
        lst = []
        item = client.recv(1024).decode(FORMAT)
        while item != "end":  
            lst.append(item)
            client.sendall(item.encode(FORMAT))
            item = client.recv(1024).decode(FORMAT)
        return lst
    
    def SignUp(self, curFrame):
        user_info = []
        try:
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
            option = SIGNUP
            client.sendall(option.encode(FORMAT))

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
                    self.show_frame(main_UI.Main_Screen)
        except Exception as e:
            print('Error: Server is not responding', str(e))
    
             
                
    def LogIn(self, curFrame):
        user_info = []   

        try:
            user_email = curFrame.text_email.get()
            password = curFrame.text_password.get()
            if user_email == "Email" or password == "Password":
                curFrame.label_notice.configure(text="Fields cannot be empty")
                return
        
            print(f"Email: {user_email}, Password: {password}")  # In ra thông tin
        
            option = LOGIN
            client.sendall(option.encode(FORMAT))
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
            
        except Exception as e:
            print('Error: Server is not responding', str(e))
    
    # def TestFrame(self):
    # show_frame(main_UI.Main_Screen)

            
    def Logout(self):
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
            else:
                print("Logout failed.")
        except Exception as e:
            print('Error: Server is not responding', str(e))


    def OpenChatBox(self):
        try:
            option = OPENCHATBOX
            client.sendall(option.encode(FORMAT))
            client.recv(1024)  # Chờ phản hồi từ server

            email = self.user_info['email']
            client.sendall(email.encode(FORMAT))

            response = self.Recv(client)  # Nhận phản hồi từ server
            print("Dữ liệu nhận được từ server:", response)
            self.Friend_list = response
            return response
        except Exception as e:
            print('Error: Server is not responding', str(e))       
            return []
       
    
    def Click_on_group_chat(self):
        try:
            option=CLICK_CHAT
            client.sendall(option.encode(FORMAT))
        except Exception as e:
            print('Error: Server is not responding', str(e)) 
            
        
# Khởi tạo client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, SERVER_PORT))

# Tạo và chạy ứng dụng
home = App()

home.mainloop()

