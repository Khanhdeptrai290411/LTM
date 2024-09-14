import socket
from customtkinter import *
import threading

HOST = "192.168.110.162"
SERVER_PORT = 65432
FORMAT = 'utf-8'
GET_CLIENTS='getclients'
class ServerPage(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x500+300+200")
        set_appearance_mode("light")
        self.configure(fg_color="#20639b")

        label_title = CTkLabel(self, text="\n ACTIVE ACCOUNT ON SERVER\n", font=("Helvetica", 18), fg_color='#20639b', bg_color="bisque2", text_color='#20639b')
        label_title.pack(pady=10)

        self.content = CTkFrame(self)
        self.data = CTkTextbox(self.content, height=10, width=40, bg_color='floral white', fg_color='floral white', font=("Helvetica", 30))

        button_log = CTkButton(self, text="REFRESH", fg_color='floral white', text_color='#20639b', hover=False, command=self.receive_data)
        button_back = CTkButton(self, text="LOG OUT", fg_color='floral white', text_color='#20639b', hover=False)
        
        button_log.pack(side=BOTTOM, pady=5)
        button_back.pack(side=BOTTOM, pady=5)

        self.content.pack(expand=True, fill=BOTH)

        self.scroll = CTkScrollbar(self.content, orientation="vertical")
        self.scroll.pack(side=RIGHT, fill=Y)

        self.data.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.data.yview)

        self.data.pack(expand=True, fill=BOTH)

        # Start a thread to receive data from server
        threading.Thread(target=self.receive_data, daemon=True).start()

    def Recv(self, client):
        data = ""
        while True:
            part = client.recv(1024).decode(FORMAT)
            if 'end' in part:
                data += part.split('end')[0]
                break
            data += part
        return data.split("\n")

    def receive_data(self):
        try:
            option = GET_CLIENTS
            client.sendall(option.encode(FORMAT))
            
            print(client.recv(1024).decode(FORMAT))
            # Receive and process the response from the server
            recv_list = self.Recv(client)
            print(recv_list)
            # Update the content of the textbox
            self.update_textbox(recv_list)
            
        except Exception as e:
            print('Error: Server is not responding', str(e))

    def update_textbox(self, items):
        # Clear current content
        self.data.delete("1.0", "end")
        # Insert new items
        for item in items:
            if item:  # Avoid inserting empty strings
                self.data.insert("end", item + "\n")

# Khởi tạo client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, SERVER_PORT))
if __name__ == "__main__":
    app = ServerPage()
    app.mainloop()
