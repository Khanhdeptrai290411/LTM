from customtkinter import *

# Tạo ứng dụng CustomTkinter
app = CTk()
app.geometry('500x400')

# Đặt chế độ sáng/tối và chủ đề
set_appearance_mode("dark")  # Sử dụng "dark" để thử nghiệm trước
set_default_color_theme("blue")  # Chủ đề mặc định

# Tạo nút đơn giản với màu sắc và viền rõ ràng
btn = CTkButton(
    master=app,
    text="click me", # Góc tròn vừa phải
    fg_color="#333333",  # Màu nền tối cho nút
    hover_color="#444444",  # Màu khi di chuột qua (sáng hơn fg_color một chút)
    border_color="#ffd700",  # Màu viền vàng
    border_width=2,
)

# Đặt vị trí cho nút
btn.place(relx=0.5, rely=0.5, anchor="center")

# Bắt đầu vòng lặp ứng dụng
app.mainloop()
