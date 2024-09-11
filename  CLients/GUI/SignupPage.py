from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import LoginPage
import socket
from datetime import datetime
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

class SignUp(CTkFrame):
    def __init__(self,parent,appController):
        super().__init__(parent)
        self.configure(width=925, height=500, fg_color='#fff')
        set_appearance_mode("light")
#-------------tao frame va anh nene----------------
        image_path = '/home/khanh/Documents/Server/ CLients/GUI/Images/login.png'
        
        image = Image.open(image_path)
        self.my_image = ImageTk.PhotoImage(image)
        image_label = Label(self, image=self.my_image, bg='white')
        image_label.place(x=50, y=50)
        
        frame = CTkFrame(self, width=350, height=350, fg_color='white')
        frame.place(x=480, y=70)
        
        
        

#--------------components-----------------------        
        heading = CTkLabel(frame, text="SIGN UP", font=("Microsoft YaHei UI Light", 24, 'bold'), text_color='#5F9EE6')
        
        dont_have_account= CTkLabel(frame,text="Don't have account?",fg_color='transparent',font=("Microsoft YaHei UI Light", 11))
        
        

#---------------user name--------
        text_user_name = PlaceholderEntry(frame, placeholder="User Name", border_width=0, width=295, fg_color='transparent', font=("Microsoft YaHei UI Light", 11))
        frame_user = CTkFrame(frame, width=295, height=2, fg_color='black')
        
            
#--------------mail--------------------        
        text_email = PlaceholderEntry(frame, placeholder="Email", border_width=0, width=295, fg_color='transparent', font=("Microsoft YaHei UI Light", 11))
        frame_email = CTkFrame(frame, width=295, height=2, fg_color='black')
           
#----------------password-------------------------------        
        text_password = PlaceholderEntry(frame, placeholder="Password", border_width=0, width=295, fg_color='transparent', font=("Microsoft YaHei UI Light", 11), show='*')
        frame_pass = CTkFrame(frame, width=295, height=2, fg_color='black')
        
        
        
        
#-----------------Button------------------------------------------------------------------        


        # button_cancel = CTkButton(frame, fg_color='red', text='Cancel', text_color='white', 
        #                           font=("Arial", 12, 'bold'), hover=False, command=self.button_cancel_action)
        button_accept = CTkButton(frame,width=265, fg_color='#5F9EE6', text='Sign up', text_color='white', 
                                  font=("Arial", 12, 'bold'), hover=True,hover_color='#9bc4ee')
        move_to_login_page= CTkButton(frame,width=6,text='Log In',border_width=0,fg_color='transparent',text_color='#5F9EE6',hover=False)
        
        
#-----------place------------------

        
        heading.place(x=100, y=5)
        text_user_name.place(x=30, y=80)
        frame_user.place(x=25, y=107)
        text_email.place(x=30, y=150)
        frame_email.place(x=25, y=177)
        text_password.place(x=30, y=220)
        frame_pass.place(x=25, y=247)
        
        # button_cancel.grid(row=0, column=0, padx=(0, 20))
        button_accept.place(x=35,y=287)
        dont_have_account.place(x=75,y=327)
        move_to_login_page.place(x=210,y=327)
        
#-----------func------------------



