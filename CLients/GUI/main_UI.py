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

        # Tạo container chính, dùng grid để chia bố cục
        main_container = CTkFrame(self)
        main_container.pack(expand=True, fill='both')
        
        # Cấu hình grid cho 2 cột
        main_container.grid_columnconfigure(0, weight=1)  # Cột 0 cho các nút bên trái
        main_container.grid_columnconfigure(1, weight=4)  # Cột 1 cho SegmentBottom

        # Nav: Tạo phần nút bên trái
        self.SegmentNav = self.Segment2(main_container, appcontroller)
        self.SegmentNav.grid(row=0, column=0, sticky='ns', padx=20, pady=20)  # Thay đổi sticky để kéo dài theo chiều dọc

        # Phần SegmentBottom bên phải
        SegmentBottom = CTkFrame(main_container, fg_color='blue',width=200)
        SegmentBottom.grid(row=0, column=1, sticky='nsew', ipadx=500, ipady=200)

        # Cấu hình hàng và cột cho SegmentBottom
        SegmentBottom.grid_rowconfigure(0, weight=1)
        SegmentBottom.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home_frame, Document_frame.Document_frame, GroupChat_frame.GroupChat_frame, Meeting_frame.Meeting_frame, Contact_frame.Contact_frame):
            frame = F(SegmentBottom, self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[F] = frame

        self.show_frame(Home_frame)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

    class Segment2(CTkFrame):
        def __init__(self, parent, appController):
            super().__init__(master=parent, fg_color='#e1e6e9')

            self.main_screen = parent

            # Tạo các nút lớn hơn
            icon_image = Image.open('/home/khanh/Documents/Server/CLients/GUI/Images/home.png')
            icon_image = CTkImage(icon_image)

            Home_button = CTkButton(self, text="Home", image=icon_image, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: self.main_screen.show_frame(Home_frame))
            document_button = CTkButton(self, text="Document", image=icon_image, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: self.main_screen.show_frame(Document_frame.Document_frame))
            contact_button = CTkButton(self, text="Contact", image=icon_image, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: self.main_screen.show_frame(Contact_frame.Contact_frame))
            group_chat_button = CTkButton(self, text="Group Chat", image=icon_image, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: self.main_screen.show_frame(GroupChat_frame.GroupChat_frame))
            meeting_button = CTkButton(self, text="Meeting", image=icon_image, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: self.main_screen.show_frame(Meeting_frame.Meeting_frame))
            back_button = CTkButton(self, text="Back", image=icon_image, compound='left', hover_color='red', fg_color='#e1e6e9',
                              text_color='#131619', font=('Arial', 24), command=lambda: self.main_screen.Logout())

            # Sắp xếp các nút
            Home_button.pack(pady=20, fill='x')
            document_button.pack(pady=20, fill='x')
            contact_button.pack(pady=20, fill='x')
            group_chat_button.pack(pady=20, fill='x')
            meeting_button.pack(pady=20, fill='x')
            back_button.pack(pady=20, fill='x')
            
            Home_button.configure(width=200, height=100)
            document_button.configure(width=200, height=100)
            contact_button.configure(width=200, height=100)
            group_chat_button.configure(width=200, height=100)
            meeting_button.configure(width=200, height=100)
            back_button.configure(width=200, height=100)

            self.pack(fill='both', side='left')

    
