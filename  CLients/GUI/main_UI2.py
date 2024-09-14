import tkinter
import customtkinter


def create_segment(self,label_text,button_text):
        frame=customtkinter.CTkFrame(master=self)
        frame.rowconfigure(0,weight=1)
        frame.columnconfigure((1,2,3),weight=1,uniform='a')
        
        #Widget
        customtkinter.CTkButton(frame,text=button_text).grid(row=0,column=2)
        customtkinter.CTkLabel(frame,text=label_text).grid(row=0,column=1)
        
        
        
        return frame
    

class Segment(customtkinter.CTkFrame):
    def __init__(self,parent,label_text,button_text):
        super().__init__(master=parent)
        
        #grid layout
        self.rowconfigure(0,weight=1)
        self.columnconfigure((0,1,2),weight=1)
        customtkinter.CTkLabel(self,text=label_text).grid(row=0,column=0,sticky='nswe')
        customtkinter.CTkButton(self,text=button_text).grid(row=0,column=1,sticky='nswe')
        segment1=self.create_segment('okdesu','adkwowad')
        
        segment1.grid(row=0,column=2,sticky='nswe')
        self.pack(expand = True,fill='both',padx=10,pady=10)
        
    def create_segment(self,label_text,button_text):
        frame=customtkinter.CTkFrame(master=self)
        frame.rowconfigure(0,weight=1)
        frame.columnconfigure((1,2,3),weight=1,uniform='a')
        
        #Widget
        customtkinter.CTkButton(frame,text=button_text).grid(row=0,column=2)
        customtkinter.CTkLabel(frame,text=label_text).grid(row=0,column=1)
        
        
        
        return frame

        

window=customtkinter.CTk()
window.title('Widget and return')
window.geometry('2000x1200')


Segment(window,'label','windows')
Segment(window,'label','windows')
Segment(window,'label','windows')
create_segment(window,'label','windows').pack(expand = True,fill='both',padx=10,pady=10)






window.mainloop()