import tkinter
import customtkinter


class Home_frame(customtkinter.CTkFrame):
    def __init__(self,parent,appcontroller,):
        super().__init__(master=parent,fg_color='blue',width=2000)
        
        CallButton=customtkinter.CTkButton(self,text='Call Now',fg_color='orange')
        Schedule_Button=customtkinter.CTkButton(self,text='Create schedule')
        
        CallButton.pack()
        Schedule_Button.pack()
        
        
        # Home_frame.pack(expand=True,fill='both')