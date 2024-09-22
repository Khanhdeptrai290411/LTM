from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import SignupPage

import bcrypt


#-------------placeholder----------
class PlaceholderEntry(CTkEntry):
    def __init__(self, master=None, placeholder="Placeholder", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = "white"
        self.default_fg_color = self.cget("fg_color")
        self._set_placeholder()
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
    
    def _set_placeholder(self):
        self.insert(0, self.placeholder)
        self.configure(fg_color=self.placeholder_color)
    
    def _on_focus_in(self, event=None):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self.configure(fg_color=self.default_fg_color)
    
    def _on_focus_out(self, event=None):
        if not self.get():
            self._set_placeholder()

class LogIn(CTkFrame):
    def __init__(self, parent, appController):
        super().__init__(parent)
        
        self.configure(width=925, height=500, fg_color='#fff')
        set_appearance_mode("light")
        appController.geometry("900x500+300+200")
        # Tạo các phần tử giao diện và hình ảnh
        image_path = 'Images/login.png'
        image = Image.open(image_path)
        self.my_image = ImageTk.PhotoImage(image)
        image_label = Label(self, image=self.my_image, bg='white')
        image_label.place(x=50, y=50)
        
        frame = CTkFrame(self, width=350, height=350, fg_color='white')
        frame.place(x=480, y=70)
        
        # Đặt các thành phần giao diện
        self.heading = CTkLabel(frame, text="LOG IN", font=("Microsoft YaHei UI Light", 24, 'bold'), text_color='#5F9EE6')
        self.already_have_account = CTkLabel(frame, text="Already have account?", fg_color='transparent', font=("Microsoft YaHei UI Light", 11))
        self.text_email = PlaceholderEntry(frame, placeholder="Email", border_width=0, width=295, fg_color='white', font=("Microsoft YaHei UI Light", 11))
        self.frame_email = CTkFrame(frame, width=295, height=2, fg_color='black')
        self.text_password = PlaceholderEntry(frame, placeholder="Password", border_width=0, width=295, fg_color='white', font=("Microsoft YaHei UI Light", 11), show='*')
        self.frame_pass = CTkFrame(frame, width=295, height=2, fg_color='black')
        self.label_notice = CTkLabel(frame, text="", fg_color='white', font=("Microsoft YaHei UI Light", 11), text_color='red', width=256)
        self.button_accept = CTkButton(frame, width=265, fg_color='#5F9EE6', text='Log In', text_color='white', font=("Arial", 12, 'bold'), hover=True, hover_color='#9bc4ee', command=lambda: (appController.LogIn()))
        self.move_to_signup_page = CTkButton(frame, width=6, text='Sign Up', border_width=0, fg_color='transparent', text_color='#5F9EE6', hover=False,command= lambda: appController.show_frame(SignupPage.SignUp))
        
        # Đặt các phần tử vào đúng vị trí
        self.heading.place(x=100, y=5)
        self.text_email.place(x=30, y=80)
        self.frame_email.place(x=25, y=107)
        self.text_password.place(x=30, y=150)
        self.frame_pass.place(x=25, y=177)
        self.button_accept.place(x=35, y=217)
        self.already_have_account.place(x=75, y=257)
        self.move_to_signup_page.place(x=230, y=257)
        self.label_notice.place(x=30, y=300)
        
    def get_email_password(self):
        email = self.text_email.get()
        password = self.text_password.get()
        return email, password    
    
#--------connect--------------
