import tkinter
import customtkinter

window=tkinter.Tk()

window.title('Pack pareting')
window.geometry('400x600')

#Frame
top_frame=customtkinter.CTkFrame(window)
bottom_frame=customtkinter.CTkFrame(window)
excersise_frame=customtkinter.CTkFrame(bottom_frame,bg_color="white")

#button
button1=customtkinter.CTkButton(excersise_frame,text="Ex1")
button2=customtkinter.CTkButton(excersise_frame,text="Ex2")
button3=customtkinter.CTkButton(excersise_frame,text="Ex3")



#widgets
label1=customtkinter.CTkLabel(top_frame,text="label",fg_color="red")
label2=customtkinter.CTkLabel(top_frame,text="label2",fg_color="blue")


#middle frame
label5=customtkinter.CTkLabel(window,text="label2",fg_color="purple")


label3=customtkinter.CTkLabel(bottom_frame,text="label3",fg_color="green")
label4=customtkinter.CTkLabel(bottom_frame,text="label3",fg_color="orange")

label1.pack(side="left",expand=True,fill="both")
label2.pack(side="left",expand=True,fill="both")
top_frame.pack(expand=True,fill="both")
label5.pack(expand=True)
label3.pack(side="left",expand=True,fill="both")
label4.pack(side="left",expand=True,fill="both")
bottom_frame.pack(side="bottom",fill="both",padx="20",pady="20")
button1.pack(side="top",fill="both",expand=True)
button2.pack(side="top",fill="both",expand=True)
button3.pack(side="top",fill="both",expand=True)
excersise_frame.pack(side="left",expand=True,fill="both")


window.mainloop()