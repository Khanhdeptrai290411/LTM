import tkinter
import customtkinter  # <- import the CustomTkinter module==============

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")

label1=tkinter.Label(root_tk,text='Label1',background='red')
label2=tkinter.Label(root_tk,text='Label2',background='red')
label3=tkinter.Label(root_tk,text='Label3',background='blue')
label4=tkinter.Label(root_tk,text='Label4',background='green')


# label1.pack(side='left',expand=True,fill='x')
# label2.pack(side='left',expand=True)

# expand , fill se lap day khoang trong theo chieu minh mon muon
#grid 
# root_tk.columnconfigure(0,weight=1)
# root_tk.columnconfigure(1,weight=1)
# root_tk.columnconfigure(2,weight=2)
# root_tk.rowconfigure(0,weight=1)
# root_tk.rowconfigure(1,weight=2)
# label1.grid(row=0,column=1,sticky='nswe',columnspan='2')

# label1.place(x=100,y=200,height=100)
# label2.place(relx=0.5,rely=0.5)
# label3.pack(side='top',expand=True,fill='both',padx=10,pady=10)
# label1.pack(side='left',expand=True,fill='both')
# label2.pack(side='bottom',expand=True,fill='both')

# label4.pack(side='bottom',expand=True,fill='both')

#Thuoc tin relx , rely, no giong nhu gan dinh label vao man hinh , ko co dinh vi tri, maf theo kich thuoc man hinh


#expand se chi mo rong 1 huong duy nhat

 
root_tk.mainloop()