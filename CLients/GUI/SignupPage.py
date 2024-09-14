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
            self.configure(fg_color='white')
    
    def _on_focus_out(self, event=None):
        if not self.get():
            self._set_placeholder()

class SignUp(CTkFrame):
    def __init__(self,parent,appController):
        super().__init__(parent)
        self.configure(width=925, height=500, fg_color='#fff')
        set_appearance_mode("light")
        appController.geometry("900x500+300+200")
#-------------tao frame va anh nene----------------
<<<<<<< HEAD: CLients/GUI/SignupPage.py
        image_path = '/media/shen/New Volume/Project/PyThonLearn/ChatPyThon/ CLients/GUI/Images/login.png'
=======
        image_path = '/home/khanh/Documents/Server/CLients/GUI/Images/login.png'
>>>>>>> UpdateServerUIv1:CLients/GUI/SignupPage.py
        
        image = Image.open(image_path)
        self.my_image = ImageTk.PhotoImage(image)
        image_label = Label(self, image=self.my_image, bg='white')
        image_label.place(x=50, y=50)
        
        frame = CTkFrame(self, width=350, height=500, fg_color='white')
        frame.place(x=480, y=50)
        
        
        

#--------------components-----------------------        
        self.heading = CTkLabel(frame, text="SIGN UP", font=("Microsoft YaHei UI Light", 24, 'bold'), text_color='#5F9EE6')
        
        self.dont_have_account= CTkLabel(frame,text="Don't have account?",fg_color='transparent',font=("Microsoft YaHei UI Light", 11))
        
        

#---------------user name--------
        self.text_user_name = PlaceholderEntry(frame, placeholder="User Name", border_width=0, width=295, fg_color='transparent', font=("Microsoft YaHei UI Light", 11))
        self.frame_user = CTkFrame(frame, width=295, height=2, fg_color='black')
        
            
#--------------mail--------------------        
        self.text_email = PlaceholderEntry(frame, placeholder="Email", border_width=0, width=295, fg_color='transparent', font=("Microsoft YaHei UI Light", 11))
        self.frame_email = CTkFrame(frame, width=295, height=2, fg_color='black')
           
#----------------password-------------------------------        
        self.text_password = PlaceholderEntry(frame, placeholder="Password", border_width=0, width=295, fg_color='transparent', font=("Microsoft YaHei UI Light", 11), show='*')
        self.frame_pass = CTkFrame(frame, width=295, height=2, fg_color='black')
        
#-------------------------notice---------------------------
        self.label_notice = CTkLabel(frame, text="", fg_color='white', font=("Microsoft YaHei UI Light", 11), text_color='red', width=256,height=20)
        
        
#-----------------Button------------------------------------------------------------------        


        # button_cancel = CTkButton(frame, fg_color='red', text='Cancel', text_color='white', 
        #                           font=("Arial", 12, 'bold'), hover=False, command=self.button_cancel_action)
        self.button_accept = CTkButton(frame,width=265, fg_color='#5F9EE6', text='Sign up', text_color='white', 
                                  font=("Arial", 12, 'bold'), hover=True,hover_color='#9bc4ee', command= lambda: appController.SignUp(self))
        self.move_to_login_page= CTkButton(frame,width=6,text='Log In',border_width=0,fg_color='transparent',text_color='#5F9EE6',hover=False,command= lambda: appController.show_frame(LoginPage.LogIn))
        
        
#-----------place------------------

        
        self.heading.place(x=100, y=5)
        self.text_user_name.place(x=30, y=80)
        self.frame_user.place(x=25, y=107)
        self.text_email.place(x=30, y=150)
        self.frame_email.place(x=25, y=177)
        self.text_password.place(x=30, y=220)
        self.frame_pass.place(x=25, y=247)
        
        # button_cancel.grid(row=0, column=0, padx=(0, 20))
        self.button_accept.place(x=35,y=287)
        self.dont_have_account.place(x=75,y=327)
        self.move_to_login_page.place(x=210,y=327)
        self.label_notice.place(x=35,y=367)
#-----------func------------------



