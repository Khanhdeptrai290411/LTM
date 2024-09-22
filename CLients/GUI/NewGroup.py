from customtkinter import *
from tkinter import BooleanVar  # Import BooleanVar để quản lý trạng thái của checkbox


class CreateGroup_frame(CTkFrame):
    def __init__(self, parent, appController):
        super().__init__(parent)
        self.appController = appController
        self.Friend_list = appController.Friend_list
        self.selected_friends = []  # Danh sách bạn bè được chọn

        # Cấu hình lưới cho frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Tạo khung chính cho giao diện
        self.create_group_interface()

    def update_friend_list(self, new_friend_list):
        self.Friend_list = new_friend_list
        print("Danh sách bạn bè trong GroupChat cập nhật:", self.Friend_list)
        self.create_group_interface()  # Làm mới danh sách bạn bè

    def create_group_interface(self):
        # Xóa các widget hiện có (để tránh trùng lặp khi cập nhật lại danh sách bạn bè)
        # for widget in self.winfo_children():
        #     widget.destroy()

        # Khung chứa danh sách bạn bè và tạo nhóm
        group_frame = CTkFrame(self, fg_color='#f4f4f4')
        group_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Tiêu đề: Nhập tên nhóm
        group_name_label = CTkLabel(group_frame, text="Enter Group Name", text_color='black', font=('Arial', 18, 'bold'))
        group_name_label.pack(pady=10)

        # Ô nhập tên nhóm
        self.group_name_entry = CTkEntry(group_frame, placeholder_text="Group Name")
        self.group_name_entry.pack(pady=10)

        # Tiêu đề: Danh sách bạn bè
        friends_title = CTkLabel(group_frame, text="Select Friends for Group", text_color='black', font=('Arial', 18, 'bold'))
        friends_title.pack(pady=10)

        # Khung cuộn cho danh sách bạn bè
        friends_scroll_frame = CTkFrame(group_frame, fg_color='#ffffff')
        friends_scroll_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Canvas để thêm thanh cuộn
        self.friends_canvas = CTkCanvas(friends_scroll_frame, bg='white')
        self.friends_canvas.pack(side='left', fill='both', expand=True)

        # Thanh cuộn cho canvas
        self.scrollbar = CTkScrollbar(friends_scroll_frame, command=self.friends_canvas.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.friends_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame đặt trong canvas để chứa danh sách checkbox bạn bè
        self.friends_frame = CTkFrame(self.friends_canvas, fg_color='white')
        self.friends_canvas.create_window((0, 0), window=self.friends_frame, anchor='nw')

        # Ràng buộc sự kiện để cập nhật vùng cuộn
        self.friends_frame.bind("<Configure>", lambda e: self.friends_canvas.configure(scrollregion=self.friends_canvas.bbox("all")))

        # Hiển thị danh sách bạn bè với checkbox
        self.checkbox_vars = {}  # Để lưu trạng thái của các checkbox
        for friend in self.Friend_list:
            self.create_friend_checkbox(self.friends_frame, friend)

        # Nút để tạo nhóm sau khi đã chọn các bạn
        create_group_btn = CTkButton(group_frame, text="Create Group", command=self.create_group)
        create_group_btn.pack(pady=10)

    def create_friend_checkbox(self, parent, friend_name):
        # Frame cho từng bạn
        friend_frame = CTkFrame(parent, fg_color='#ffffff', corner_radius=5)
        friend_frame.pack(fill='x', padx=10, pady=5)

        # Biến lưu trạng thái của checkbox
        var = BooleanVar()
        self.checkbox_vars[friend_name] = var

        # Tạo checkbox cho từng người bạn
        friend_checkbox = CTkCheckBox(friend_frame, text=friend_name, variable=var, onvalue=True, offvalue=False)
        friend_checkbox.pack(side='left', padx=10, pady=10)

    def create_group(self):
        # Lấy danh sách bạn bè được chọn
        self.selected_friends = [friend for friend, var in self.checkbox_vars.items() if var.get()]
        self.group_name = self.group_name_entry.get()  # Lấy tên nhóm từ ô nhập
        
        if self.selected_friends and self.group_name:
            print(f"Group '{self.group_name}' created with members: {', '.join(self.selected_friends)}")
            self.appController.createGroup()
            # Bạn có thể gửi thông tin này về appController để xử lý tiếp
        elif not self.group_name:
            print("Please enter a group name")
        else:
            print("No members selected to create a group")
    