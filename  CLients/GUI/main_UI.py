import tkinter
import customtkinter
from PIL import Image, ImageTk

from Home_frame import Home_frame
import Document_frame
import GroupChat_frame
import Meeting_frame
import Contact_frame

import LoginPage


HOME_PATH=''



## Luu y ta co app controller 

class Main_Screen(customtkinter.CTkFrame):
    def __init__(self,parent,appcontroller):
        super().__init__(parent,fg_color='#ffffff')
   
        self.appcontroller=appcontroller
        SegmentBottom=Home_frame(self,'vailone')
        appcontroller.geometry("2000x900")
        self.SegmentNav= self.Segment2(self,appcontroller)
        self.SegmentNav.pack(side='top',fill='both',expand=True)
    # Segment(window,'qeqew','qweqwe')
        SegmentBottom.pack(side='bottom',expand=True,fill='both')  
        self.frames={}
        for F in (Home_frame,Document_frame.Document_frame,Home_frame,GroupChat_frame.GroupChat_frame,Contact_frame.Contact_frame):
            frame=F(SegmentBottom,appcontroller)
            frame.grid(row=0, column=0, sticky='nsew')

            self.frames[F]=frame
        self.changeFrame('Home')
    
    def backToLoginFrame(self):
        self.appcontroller.show_frame(LoginPage.LogIn)

    
    def changeFrame(self,NameFrame):
          if(NameFrame=='Document'):
              frame=self.frames[Document_frame.Document_frame]
              frame.tkraise()
          elif(NameFrame=='Meeting'):
              frame=self.frames[Meeting_frame.Meeting_frame]
              frame.tkraise()
          elif(NameFrame=='Group Chat'):
              frame=self.frames[GroupChat_frame.GroupChat_frame]
              frame.tkraise()
          elif(NameFrame=='Contact'):
              frame=self.frames[Contact_frame.Contact_frame]
              frame.tkraise()
          elif(NameFrame=='Home'):
              frame=self.frames[Home_frame]
              frame.tkraise()
        
        
        

    # class Segment2(customtkinter.CTkFrame):
    #     def __init__(self,parent,label_text,button_text):
    #         super().__init__(master=parent)
            
            
            
    #         # self.rowconfigure(0,weight=1)
    #         # self.columnconfigure((0,1,2),weight=1)
    #         Home_button=self.creatButton('Home','icon')
    #         document_button=self.creatButton('Document ','icon')
    #         contact_button=self.creatButton('Contact','icon')
    #         group_chat_button=self.creatButton('Group chat','icon')
    #         meeting_button=self.creatButton('Meeting','icon')

    #         Home_button.pack(side='left')
    #         document_button.pack(side='left')
    #         contact_button.pack(side='left')
    #         group_chat_button.pack(side='left')
    #         meeting_button.pack(side='left')

            
    #         self.pack(expand=True,fill='both',side='bottom')
            
    #     def creatButton(self,label_text,icon):
    #         icon_image = Image.open('images/home.png')

    #         icon_image=customtkinter.CTkImage(icon_image)
    #         label=customtkinter.CTkButton(self,text=label_text,image=icon_image,compound='left',hover_color='red',padx=50)
    #         return label
    
    
    class Segment2(customtkinter.CTkFrame):
            

        def __init__(self,parent,appController):
            super().__init__(master=parent,height=50,fg_color='#e1e6e9')

            self.main_screen=parent
            
            self.currentButton=None
            self.lastButton=None
                
                # self.rowconfigure(0,weight=1)
                # self.columnconfigure((0,1,2),weight=1)
            Home_button=self.creatButton('Home','icon')
            # self.doimau(Home_button)
            Home_button.configure(command=lambda: self.main_screen.changeFrame('Home'))
            document_button=self.creatButton('Document ','icon')
            contact_button=self.creatButton('Contact','icon')
            group_chat_button=self.creatButton('Group chat','icon')
            meeting_button=self.creatButton('Meeting','icon')
            back_button=self.creatButton('back','icon')
                
                
                
                
            document_button.configure(command=lambda: (self.doimau(contact_button),self.main_screen.changeFrame('Document')))
            contact_button.configure(command=lambda: (self.doimau(contact_button),self.main_screen.changeFrame('Contact')))
            group_chat_button.configure(command=lambda: (self.doimau(group_chat_button),self.main_screen.changeFrame('Group Chat')))
            meeting_button.configure(command=lambda: (self.doimau(meeting_button),self.main_screen.changeFrame('Group Chat')))
            back_button.configure(command=lambda: (self.doimau(back_button),self.main_screen.backToLoginFrame()))
   
            Home_button.pack(side='left')
            document_button.pack(side='left')
            contact_button.pack(side='left')
            group_chat_button.pack(side='left')
            meeting_button.pack(side='left')
            back_button.pack(side='left')
                
            self.pack(fill='both',side='top')
                
        def creatButton(self,label_text,icon):
            icon_image = Image.open('images/home.png')

            icon_image=customtkinter.CTkImage(icon_image)
        
            label=customtkinter.CTkButton(self,text=label_text,image=icon_image,compound='left',hover_color='red',fg_color='#e1e6e9',text_color='#131619',font=('Arial',50))
            label.configure(width=200, height=80)
            return label

            
        def doimau(self,buttonChange):
                self.lastButton=self.currentButton
                self.currentButton=buttonChange
                
                self.currentButton.configure(fg_color='#ffffff')
                if(self.lastButton):
                    self.lastButton.configure(fg_color='#e1e6e9')
                    self.lastButton=None

            


    
   
    
        
        
      

            
    









        
# window.title('Meeting Chat')
# window.geometry('2500x1500')



# # Segment2(window,'qwewqeqew','qeqwqwe2121')


# window.mainloop()