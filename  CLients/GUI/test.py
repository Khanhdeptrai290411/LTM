from customtkinter import *

app = CTk()
app.geometry('900x500')

#-------layout-------
first_layout = CTkFrame(app)
second_layout = CTkFrame(app)
#-------place layout------
first_layout.place(x=0,y=0,relwidth=0.3,relheight=1)
second_layout.place(relx=0.3,y=0,relwidth=0.7,relheight=1)


# CTkLabel(first_layout, fg_color='red').pack(expand=True, fill='both')
# CTkLabel(second_layout, fg_color='yellow').pack(expand=True, fill='both')

#------------components------------
button1 = CTkButton(first_layout,text='button1',hover=False)
button2 = CTkButton(first_layout,text='button2')
button3 = CTkButton(first_layout,text='button3')

slider1= CTkSlider(first_layout,orientation='vertical')
slider2= CTkSlider(first_layout,orientation='vertical')

#------------grid layout----------
#create grid
first_layout.columnconfigure((0,1,2),weight=2,uniform='a')
first_layout.rowconfigure((0,1,2,3,4),weight=2,uniform='a')
#components in grid
button1.grid(row=0, column=0, sticky='nswe', columnspan=2, padx=10, pady=10)
button2.grid(row=0, column=2, sticky='nswe', padx=10, pady=10)
button3.grid(row=1, column=0, sticky='nswe', columnspan=3, padx=10, pady=10)

app.mainloop()