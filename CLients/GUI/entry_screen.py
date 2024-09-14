import tkinter
import customtkinter
from PIL import Image



def OpenSignUpScreen(event):
    import testUi
    
    
window = tkinter.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Poom Meeting")

# Đặt kích thước mặc định cho cửa sổ, ví dụ: 800x600
window.geometry('1024x800')
window.configure()
def main():
 # Tạo cửa sổ chính



    #image
    # bg=tkinter.PhotoImage(file="images/entrybackground.png")
    bg=customtkinter.CTkImage(light_image=Image.open("images/entrybackground.png"),size=(75,45))


    #frame
    frameLeft=customtkinter.CTkFrame(window)
    frameRight=customtkinter.CTkFrame(window,fg_color="white")


    #widget


    Label=customtkinter.CTkLabel(frameLeft,image=bg)
    LabelTop=customtkinter.CTkLabel(frameRight,text='Welcome To Poom Meeting',text_color='#5f9EE6',font=("Arial",40))
    LabelStart=customtkinter.CTkLabel(frameRight,text="Let's start" ,text_color='#5f9EE6',font=("Arial",40))



    #button
    LabelStart.bind('<Button-1>',OpenSignUpScreen)


    Label.pack(side="left",expand=True,fill='both')
    LabelTop.pack(side="top",expand=True,fill='both')
    LabelStart.pack(side="top",expand=True,fill='both')
    frameLeft.pack(side="left",expand=True,fill='both')
    frameRight.pack(side="left",expand=True,fill="both")   



    # Chạy vòng lặp chính để hiển thị cửa sổ
main()
window.mainloop()
