from customtkinter import *

class ServerPage(CTkFrame):
    def __init__(self, parent, appController):
        super().__init__(parent)
        self.controller = appController  # For switching between frames
        self.setup_frame()
        self.Friend_list = []

    def setup_frame(self):
        """ Set up the frame layout. """
        # Frame title
        label_title = CTkLabel(self, text="\n ACTIVE ACCOUNT ON SERVER\n", font=("Helvetica", 18), fg_color='#20639b', bg_color="bisque2", text_color='#20639b')
        label_title.pack(pady=10)

        # Content frame for displaying the list of users
        self.content = CTkFrame(self)
        self.content.pack(expand=True, fill=BOTH)

        # Log out button (can trigger a controller method to log out)
        button_back = CTkButton(self, text="LOG OUT", fg_color='floral white', text_color='#20639b', hover=False, command=self.logout)
        button_back.pack(side=BOTTOM, pady=5)

    def logout(self):
        """ Handle logout action (delegate to controller). """
        self.controller.Logout()  # Assuming `controller` has a logout method.

    def update_friend_list(self, lst):
        """ Update the frame with the latest room data (list of users). """
        try:
            # Clear the previous list
            for widget in self.content.winfo_children():
                widget.destroy()

            self.Friend_list = lst
            print("Danh sách bạn bè cập nhật:", self.Friend_list)

            # Update the frame with new user list
            for friend in self.Friend_list:
                if friend:
                    self.add_user_to_list(friend)

        except Exception as e:
            print(f"Error in update_room: {str(e)}")

    def add_user_to_list(self, friend):
        """ Add a single user to the displayed list with a 'Kick' button. """
        frame = CTkFrame(self.content)
        frame.pack(fill=X, pady=5)

        label = CTkLabel(frame, text=friend, font=("Helvetica", 34))
        label.pack(side=LEFT, padx=10, pady=5)

        kick_button = CTkButton(frame, text="Kick", fg_color='red', text_color='white', command=lambda f=friend: self.controller.kick_user(f))
        kick_button.pack(side=RIGHT, padx=10)

    
