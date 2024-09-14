from customtkinter import *
import tkinter
from PIL import Image  # Import PIL để mở hình ảnh
import socket
import SignupPage
import LoginPage
import EntryPage
import HomePage



import bcrypt
HOST = "192.168.110.162"
SERVER_PORT = 65433
FORMAT = "utf8"
OK = 'ok'
LOGIN='login'
SIGNUP='signup'
FAIL='fail'
END='x'
class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x500+300+200")
        set_appearance_mode("light")  # Bạn có thể chuyển thành "dark" để thử nghiệm
        self.title("C")
        
        #--------components----------------
        container = CTkFrame(self)  # Đảm bảo container có master
        container.pack(fill="both", expand=True)
        
        # Dictionary to hold frames
        self.frames = {}
        
        for F in (SignupPage.SignUp, LoginPage.LogIn, EntryPage.Entry,HomePage.Home):  # Sử dụng các lớp, không phải module
            frame = F(container, self)  # Tạo một frame từ lớp đã nhập
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[F] = frame
        
        # Hiển thị frame đầu tiên (EntryPage)
        self.show_frame(EntryPage.Entry)
    
    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()
        
    
    def sendList(self,client, list):
        for item in list:
            client.sendall(item.encode(FORMAT))
            client.recv(1024)
        msg = "end"
        client.send(msg.encode(FORMAT))
    
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
                    self.show_frame(HomePage.Home)
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
                self.show_frame(HomePage.Home)
            
        except Exception as e:
            print('Error: Server is not responding', str(e))
            
            
    


# Khởi tạo client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, SERVER_PORT))

# Tạo và chạy ứng dụng
home = App()
home.mainloop()
