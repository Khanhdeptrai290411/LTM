from customtkinter import *
from PIL import Image, ImageTk

from Home_frame import Home_frame
import Document_frame
import GroupChat_frame
import Meeting_frame
import Contact_frame

class Main_Screen(CTkFrame):
    def __init__(self, parent, appcontroller):
        super().__init__(parent, fg_color='#ffffff')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        self.appcontroller = appcontroller
        self.Friend_list = appcontroller.Friend_list
        
        
        # Cấu hình grid cho 2 cột
        self.grid_columnconfigure(0, weight=1)  # Cột 0 cho các nút bên trái
        self.grid_columnconfigure(1, weight=4)  # Cột 1 cho SegmentBottom


        # Nav: Tạo phần nút bên trái
        self.SegmentNav = self.Segment2(self, appcontroller)
        self.SegmentNav.grid(row=0, column=0, sticky='ns', ipadx=30, ipady=20)  # Thay đổi sticky để kéo dài theo chiều dọc

        # Phần SegmentBottom bên phải
        SegmentBottom = CTkFrame(self, fg_color='blue',width=200)
        SegmentBottom.grid(row=0, column=1, sticky='nsew', ipadx=170)
        SegmentBottom.grid_rowconfigure(0, weight=1)
        SegmentBottom.grid_columnconfigure(0, weight=1)

        # Cấu self
        self.frames = {}
        for F in (Home_frame, Document_frame.Document_frame, GroupChat_frame.GroupChat_frame, Meeting_frame.Meeting_frame, Contact_frame.Contact_frame):
            frame = F(SegmentBottom, self.appcontroller)
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[F] = frame

        self.show_frame(Document_frame.Document_frame)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()
        
        
        
    def update_friend_list(self, new_friend_list):
            self.Friend_list = new_friend_list
            print("new Friends", self.Friend_list)

    def update_group_screen(self,appController):
        appController.OpenChatBox()
        # Cập nhật Main_Screen với Friend_list mới
        if hasattr(self, 'frames') and GroupChat_frame.GroupChat_frame in self.frames:
            group_screen = self.frames[GroupChat_frame.GroupChat_frame]
            group_screen.update_friend_list(self.Friend_list)         
            
    class Segment2(CTkFrame):
        def __init__(self, parent, appController):
            super().__init__(master=parent, fg_color='#e1e6e9')

            self.main_screen = parent
            self.Friend_list = parent.Friend_list
            
            # Tạo các nút lớn hơn
            home_icon = Image.open('/home/khanh/Documents/Server/CLients/GUI/Images/home.png')
            home_icon = CTkImage(home_icon)
            
            document_icon = Image.open('/home/khanh/Documents/Server/CLients/GUI/Images/document.png')
            document_icon = CTkImage(document_icon)
            
            contact_icon = Image.open('/home/khanh/Documents/Server/CLients/GUI/Images/contact.png')
            contact_icon = CTkImage(contact_icon)
            
            groupchat_icon = Image.open('/home/khanh/Documents/Server/CLients/GUI/Images/groupchat.png')
            groupchat_icon = CTkImage(groupchat_icon)
            
            meeting_icon = Image.open('/home/khanh/Documents/Server/CLients/GUI/Images/meeting.png')
            meeting_icon = CTkImage(meeting_icon)
            
            back_icon = Image.open('/home/khanh/Documents/Server/CLients/GUI/Images/back.png')
            back_icon = CTkImage(back_icon)
            
            Home_button = CTkButton(self, image=home_icon, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda:(parent.show_frame(Home_frame),appController.OpenChatBox()) )
            document_button = CTkButton(self, text="Document", image=document_icon, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: parent.show_frame(Document_frame.Document_frame))
            contact_button = CTkButton(self, text="Request", image=contact_icon, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: parent.show_frame(Contact_frame.Contact_frame))
            group_chat_button = CTkButton(self, text="Chat", image=groupchat_icon, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda:(parent.show_frame(GroupChat_frame.GroupChat_frame),self.main_screen.update_group_screen(appController)) )
            meeting_button = CTkButton(self, text="Meeting", image=meeting_icon, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: parent.show_frame(Meeting_frame.Meeting_frame))
            back_button = CTkButton(self, text="Back", image=back_icon, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: appController.Logout())

            # Sắp xếp các nút
            Home_button.pack(pady=20, fill='x')
            document_button.pack(pady=20, fill='x')
            contact_button.pack(pady=20, fill='x')
            group_chat_button.pack(pady=20, fill='x')
            meeting_button.pack(pady=20, fill='x')
            back_button.pack(pady=20, fill='x')
            
            Home_button.configure(text='Home',width=200, height=100)
            document_button.configure(width=200, height=100)
            contact_button.configure(width=200, height=100)
            group_chat_button.configure(width=200, height=100)
            meeting_button.configure(width=200, height=100)
            back_button.configure(width=200, height=100)

            self.pack(fill='both', side='left')

        def print_friend_list(self,ok):
            print("Danh sách bạn bè trong Segment2:", ok)
            
        def update_group_screen(self,appController):
            appController.OpenChatBox()
            # Cập nhật Main_Screen với Friend_list mới
            if hasattr(self, 'frames') and GroupChat_frame.GroupChat_frame in self.frames:
                group_screen = self.frames[GroupChat_frame.GroupChat_frame]
                group_screen.update_friend_list(self.Friend_list)