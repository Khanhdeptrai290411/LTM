from customtkinter import *
from PIL import Image  # Import PIL để mở hình ảnh


class Home(CTkFrame):
    def __init__(self,parent,appController):
        super().__init__(parent)
        set_appearance_mode("light")  # Bạn có thể chuyển thành "dark" để thử nghiệm
        #--------components
        label=CTkLabel(self,text="Home")
        label.pack()
        
    
