from customtkinter import *
from PIL import Image  # Import PIL để mở hình ảnh
from tkinter import *
import LoginPage
import SignupPage

class Entry(CTkFrame):
    def __init__(self, parent,appController):
        super().__init__(parent)
        self.configure(width=925, height=500, fg_color='#fff')
        set_appearance_mode("light")


        # --------components
        label = CTkLabel(self, text="Entry")
        label.pack()
        
        button = CTkButton(self, text='Login',command=lambda: appController.show_frame(LoginPage.LogIn))
        button.pack()
        
        button2 = CTkButton(self, text='Signup',command=lambda: appController.show_frame(SignupPage.SignUp))
        button2.pack()



