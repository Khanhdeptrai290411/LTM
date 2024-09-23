import threading
import time
from customtkinter import *
import tkinter
from PIL import Image  # Import PIL để mở hình ảnh
import socket
import LoginAdmin
import ServerUI



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
HOST = "192.168.1.189"
SERVER_PORT = 65438
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
class App(CTk):
    
    def __init__(self):
        super().__init__()
        self.geometry("900x500+300+200+700")
        set_appearance_mode("light")  # Bạn có thể chuyển thành "dark" để thử nghiệm
        
        self.User_info=[]
        self.user_info=[]
        self.Friend_list=[]
        self.user_to_kick=None
        self.title('C')

        #--------components----------------
        container = CTkFrame(self)  # Đảm bảo container có master
        container.pack(fill="both", expand=True)
        
        # Dictionary to hold frames
        self.frames = {}
        
        for F in (LoginAdmin.LogIn,ServerUI.ServerPage):  # Sử dụng các lớp, không phải module
            frame = F(container, self)  # Tạo một frame từ lớp đã nhập
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[F] = frame
        
        # Hiển thị frame đầu tiên (EntryPage)
        self.show_frame(LoginAdmin.LogIn)
    
    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()
            
            
            
 
    
    
    
    
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
            if(user_email=='admin'):
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
                    self.title(self.user_info.get('email') if self.user_info else 'C')
                    self.show_frame(ServerUI.ServerPage)
            else:
                curFrame.label_notice.configure(text="Not admin")
                return
            # if(response=="User not found"):
            #     curFrame.label_notice.configure(text="User not found")
            #     return
            # elif(response==FAIL):
            #     curFrame.label_notice.configure(text="Invalid Password")
            #     return
            # else:
            #     lst = self.User_info_Recv(client)
            #     self.User_info = lst
            #     fields = self.User_info[0].split(',')
            #     self.user_info = {
            #         'user_id': fields[0],
            #         'user_name': fields[1],
            #         'email': fields[2],
            #         'password_hash': fields[3],
            #         'ip_address': fields[4],
            #         'status': fields[5],
            #         'created_at': fields[6]
            #     }
            #     print(self.user_info['user_name'])
            #     self.show_frame(ServerUI.ServerPage)
            #     self.title(self.user_info.get('email') if self.user_info else 'C')
            #     print("da chay xong loginuser")

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
                self.show_frame(LoginAdmin.LogIn)
                
                client.close()
                print('disconnected from server')
            else:
                print("Logout failed.")
        except Exception as e:
            print('Error: Server is not responding', str(e))
   
    def kick_user(self,user):
        option = KICK_USER
        client.sendall(option.encode(FORMAT))
        self.user_to_kick=user
    def kick_user_onl(self):
        option = KICK_USER
        client.sendall(option.encode(FORMAT))
        client.recv(1024)
        email = self.user_to_kick
        client.sendall(email.encode(FORMAT))
        print(f"Đã gửi yêu cầu kick user: {email}")
        
    def handleClient(self):
        while self.connected:
            print(f'dang o {client} ')
            data = client.recv(1024).decode(FORMAT) # nhan lan 1 cua handle ben server
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
                    self.LogInUser(self.frames[LoginAdmin.LogIn])
                elif data == KICK_USER:
                    self.kick_user_onl()
                
 
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
        if hasattr(self, 'frames') and ServerUI.ServerPage in self.frames:
            main_screen = self.frames[ServerUI.ServerPage]
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


            
               



# Tạo và chạy ứng dụng
home = App()
# home.connect_to_server()
home.mainloop()