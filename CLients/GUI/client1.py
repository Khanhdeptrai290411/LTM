import socket
import threading
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

class ChatClient(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chat Client")
        self.geometry("600x400")

        # Text area
        self.text_area = ctk.CTkTextbox(self, width=500, height=250)
        self.text_area.pack(pady=10)
        self.text_area.configure(state="disabled")

        # Input field and buttons
        self.input_field = ctk.CTkEntry(self, width=400)
        self.input_field.pack(pady=5)
        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.send_file_button = ctk.CTkButton(self, text="Send File", command=self.send_file)
        self.send_file_button.pack(pady=5)

        self.file_dropdown = ctk.CTkOptionMenu(self, values=["Select a file to download"], command=self.request_file)
        self.file_dropdown.pack(pady=5)

        # Socket setup
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(('192.168.1.189', 12344))
            threading.Thread(target=self.receive_messages, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to server: {e}")
            self.destroy()

    def send_message(self):
        message = self.input_field.get()
        if message:
            try:
                self.socket.sendall(b"TEXT\n" + message.encode())
                self.input_field.delete(0, 'end')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send message: {e}")

    def send_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            try:
                with open(file_path, 'rb') as f:
                    file_data = f.read()

                self.socket.sendall(b"FILE\n" + file_name.encode() + b"\n" + str(file_size).encode())
                self.socket.sendall(file_data)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send file: {e}")

    def request_file(self, file_name):
        if file_name != "Select a file to download":
            try:
                self.socket.sendall(b"REQUEST_FILE\n" + file_name.encode())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to request file: {e}")

    def receive_messages(self):
        try:
            while True:
                # Đọc loại tin nhắn
                message_type = self.socket.recv(1024).decode().strip()
                print(f"Received message type: {message_type}")  # In ra loại tin nhắn nhận được

                if not message_type:
                    break  # Nếu không nhận được dữ liệu, thoát vòng lặp

                if message_type == "TEXT":
                    # Đọc phần tin nhắn
                    message = self.socket.recv(1024).decode()
                    print(f"Message received: {message}")  # In ra để debug

                    # Hiển thị tin nhắn lên giao diện
                    self.text_area.configure(state="normal")
                    self.text_area.insert('end', message + "\n")
                    self.text_area.configure(state="disabled")

                elif message_type == "FILE":
                    file_name = self.socket.recv(1024).decode()
                    file_size = int(self.socket.recv(1024).decode())
                    file_data = self.socket.recv(file_size)

                    # Lưu file
                    with open(f"received_{file_name}", 'wb') as f:
                        f.write(file_data)

                    # Cập nhật dropdown tệp
                    current_files = list(self.file_dropdown["values"])
                    if file_name not in current_files:
                        current_files.append(file_name)
                        self.file_dropdown.configure(values=current_files)
                    
                    messagebox.showinfo("File Downloaded", f"Received file: {file_name}")

        except Exception as e:
            print(f"Error in receive_messages: {e}")  # In ra lỗi nếu có
            messagebox.showerror("Error", f"Connection lost: {e}")
            self.destroy()



if __name__ == "__main__":
    app = ChatClient()
    app.mainloop()
