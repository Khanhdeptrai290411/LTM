import tkinter
import customtkinter


class Home_frame(customtkinter.CTkFrame):
    def __init__(self,parent,appcontroller,):
        super().__init__(master=parent,fg_color='red')
        
        CallButton=customtkinter.CTkButton(self,text='Call Now',fg_color='orange')
        Schedule_Button=customtkinter.CTkButton(self,text='Create schedule')
        
        self.columnconfigure((0,1,2),weight=1)
        self.rowconfigure(0,weight=1)
        CallButton.grid(row=0,column=1)
        Schedule_Button.grid(row=0,column=2)
        
        
        # Home_frame.pack(expand=True,fill='both')