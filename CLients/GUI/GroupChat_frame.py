from customtkinter import *
from PIL import Image  # Để load hình ảnh

class GroupChat_frame(CTkFrame):
    def __init__(self,parent,appController):
        super().__init__(parent)

        
        self.appController=appController
        self.Friend_list = appController.Friend_list
        self.group_list = appController.Group_list
        self.Header_Name=[]
        self.CurrentGroupId='1'
        # Cấu hình grid tổng thể
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=9)  # Hàng thứ hai cho phần chat lớn hơn

        # Tạo khu vực tên người dùng và icon call trên đầu
        # self.create_chat_header()

        # Khu vực chat chính giữa có thanh cuộn cho nội dung tin nhắn
        self.create_chat_body()

        # Khu vực danh sách bạn bè bên phải
        self.ListFrame=CTkFrame(self)
        self.ListFrame.grid(column=2,row=0,rowspan=9,sticky='nsew',padx=5,pady=5)
                    # chat_body.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

        self.create_friends_list(self.ListFrame)
        self.create_groups_list(self.ListFrame)
    def Update_ChatGroup_List(self,FriendList,GroupList):
        self.Friend_list=FriendList
        self.group_list=GroupList
        # self.ListFrame.destroy()
        self.ListFrame=CTkFrame(self)
        self.ListFrame.grid(column=2,row=0,rowspan=9,sticky='nsew',padx=5,pady=5)
        self.create_friends_list(self.ListFrame)
        self.create_groups_list(self.ListFrame)
        
    def Change_header_name(self):
        self.Header=['hello']
        self.create_chat_header(self.Header[0])
        
        
    def create_chat_header(self,username):
        # Load icon call
        contact_icon = Image.open('Images/contact.png')
        contact_icon = CTkImage(contact_icon, size=(30, 30))

        # Tạo khung chứa tên người dùng và icon call
        chat_header = CTkFrame(self, fg_color='#0a84ff', height=60)
        chat_header.grid(row=0, column=1, sticky='ew', padx=10, pady=(10, 0))

        # Thêm tên người đang chat
        self.chat_name_label = CTkLabel(chat_header, text=username, text_color='white', font=('Arial', 20, 'bold'))
        self.chat_name_label.pack(side='left', padx=20, pady=10)

        # Thêm nút gọi với icon
        self.call_button = CTkButton(chat_header, image=contact_icon, text="", width=50, fg_color='#0a84ff',
                                     hover_color='#0062cc', corner_radius=10)
        self.call_button.pack(side='right', padx=20, pady=10)
        

    def create_chat_body(self):
        # Khung chính của khu vực chat
        chat_body = CTkFrame(self, fg_color='#eaeaea')
        chat_body.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

        # Khung chính để chứa nội dung tin nhắn có thanh cuộn
        chat_scroll_frame = CTkFrame(chat_body, fg_color='#ffffff')
        chat_scroll_frame.pack(expand=True, fill='both', padx=5, pady=5)

        # Canvas để thêm thanh cuộn
        self.message_canvas = CTkCanvas(chat_scroll_frame, bg='white')
        self.message_canvas.pack(side='left', fill='both', expand=True)

        # Thanh cuộn cho canvas
        self.scrollbar = CTkScrollbar(chat_scroll_frame, command=self.message_canvas.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.message_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame đặt trong canvas để chứa tin nhắn
        self.message_frame = CTkFrame(self.message_canvas, fg_color='white')
        self.message_canvas.create_window((0, 0), window=self.message_frame, anchor='nw')

        self.message_frame.bind("<Configure>", lambda e: self.message_canvas.configure(scrollregion=self.message_canvas.bbox("all")))

        # Tin nhắn từ người khác (bên trái)
        self.display_message(self.message_frame, "Hello! How are you?", False)

        # Tin nhắn của mình (bên phải)
        self.display_message(self.message_frame, "I'm good, thank you!", True)

        # Khung để nhập tin nhắn
        self.input_frame = CTkFrame(chat_body, fg_color='#dfe3e6')
        self.input_frame.pack(fill='x', padx=10, pady=(0, 10))

        # Thêm khung nhập Friend_listăn bản
        self.message_entry = CTkEntry(self.input_frame, placeholder_text="Type a message", width=500)
        self.message_entry.pack(side='left', padx=5, pady=5)
        
        # Nút gửi tin nhắn
        send_button = CTkButton(self.input_frame, text="Send", command= lambda:(self.appController.sendMessage(self,self.CurrentGroupId)))
        send_button.pack(side='right', padx=5, pady=5)

    def display_message(self, parent, message, is_self):
        # Khung chính cho tin nhắn
        msg_frame = CTkFrame(parent, fg_color='#d1e8ff' if is_self else '#ffffff', corner_radius=10)
        
        # Tạo lưới cho parent
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)

        if is_self:
            # Nếu là tin nhắn của mình thì ở cột bên phải
            msg_frame.grid(row=len(parent.winfo_children()), column=1, sticky='e', padx=(250, 10), pady=5)
        else:
            # Nếu là tin nhắn của người khác thì ở cột bên trái
            msg_frame.grid(row=len(parent.winfo_children()), column=0, sticky='w', padx=(10, 50), pady=5)

        # Nội dung tin nhắn
        msg_label = CTkLabel(msg_frame, text=message, text_color='black', font=('Arial', 14), padx=10, pady=5)
        msg_label.pack(fill='x')

    # def send_message(self):
    #     # Lấy tin nhắn từ khung nhập
    #     message = self.message_entry.get()
    #     if message.strip() != "":

    #         # Hiển thị tin nhắn của mình
    #         self.display_message(self.message_frame, message, True)   
    #         # Xóa nội dung nhập
    #         self.message_entry.delete(0, 'end')
    
    def update_friend_list(self, new_friend_list):
        self.Friend_list = new_friend_list
        print("Danh sách bạn bè trong GroupChat cập nhật:", self.Friend_list)
        self.create_friends_list(self.ListFrame)  # Hàm này sẽ làm mới danh sách bạn bè

    def update_group_list(self,new_group_list):
        self.group_list=new_group_list
        print("Danh sach Group duoc cap nhap la:",self.group_list)
        self.create_groups_list(self.ListFrame)
    # Xu li su kien khi nhan nut openChat
    def OpenWindowChat(self,group_id):
        option="open_window_chat"
        self.appController.sendall(option)
        
        print("Danh sach Group duoc cap nhap la:",self.group_list)
        self.create_groups_list(self.ListFrame)
   
    
        
        
    def create_friends_list(self,parent):
        friends_list = CTkFrame(parent, fg_color='#f4f4f4')
        friends_list.pack(side='top', expand=True,fill='both', padx=5, pady=5)

        # Tiêu đề danh sách bạn bè
        friends_title = CTkLabel(friends_list, text="Friends", text_color='black', font=('Arial', 18, 'bold'))
        friends_title.pack(pady=5)

        # Hiển thị danh sách bạn bè
        friends = self.Friend_list
        for friend in friends:
            self.create_friend_item(friends_list, friend)

    def create_friend_item(self, parent, friend_name):
        friend_frame = CTkFrame(parent, fg_color='#ffffff', corner_radius=5)
        friend_frame.pack(fill='x', padx=5, pady=5)

        # Tên bạn bè
        friend_label = CTkButton(friend_frame, text=friend_name, text_color='black', font=('Arial', 16), anchor='w')
        friend_label.pack(side='left', padx=5, pady=5)
    
    
    def create_groups_list(self,parent):
        print("Goi create_group_list frame")
        # Place the group list in row 2, right below the friends list
        groups_list = CTkFrame(parent, fg_color='#f4f4f4')
        groups_list.pack(side='top', expand=True,fill='both', padx=5, pady=5)

        # Tiêu đề danh sách nhóm
        groups_title = CTkLabel(groups_list, text="Groups", text_color='black', font=('Arial', 18, 'bold'))
        groups_title.pack(pady=5)

        # # Hiển thị tên nhóm hiện tại
        # current_group_label = CTkLabel(groups_list, text="Current Group: " + self.appController.current_group, 
        #                             text_color='black', font=('Arial', 16, 'italic'))
        # current_group_label.pack(pady=5)

        # Hiển thị danh sách nhóm
        groups = self.appController.Group_list  # Assuming Group_list is available in appController
        for group in groups:
            group_id=group[0]
            group_name=group[1]
            self.create_group_item(groups_list, group_name,group_id)

    def create_group_item(self, parent, group_name):
        # Tạo khung cho mỗi nhóm
        group_frame = CTkFrame(parent, fg_color='#ffffff', corner_radius=5)
        group_frame.pack(fill='x', padx=5, pady=5)

        # Nút tên nhóm
        group_label = CTkButton(group_frame, text=group_name, text_color='black', font=('Arial', 16), anchor='w')
        group_label.pack(side='left', padx=5, pady=5)