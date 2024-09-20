import socket
import threading
import os

clients = {}
server_files = {}

def broadcast_message(message, client_to_exclude=None):
    for client, client_name in clients.items():
        if client != client_to_exclude:
            try:
                print(f"Sending message to {client_name}: {message}")  # In ra để debug
                client.sendall(f"TEXT\n{message}\n".encode())  # Gửi tin nhắn
            except Exception as e:
                print(f"Failed to send message to {client_name}: {e}")



def broadcast_file(file_data, file_name, client_to_exclude):
    for client, client_name in clients.items():
        if client != client_to_exclude:
            try:
                client.sendall(f"FILE\n{file_name}\n{len(file_data)}".encode())
                client.sendall(file_data)
            except Exception as e:
                print(f"Failed to send file to {client_name}: {e}")

def handle_client(client_socket, client_name):
    try:
        while True:
            # Nhận loại tin nhắn từ client
            message_type = client_socket.recv(1024).decode().strip()
            print(f"Received message type: {message_type} from {client_name}")  # Debug loại tin nhắn

            if message_type == "TEXT":
                message = client_socket.recv(1024).decode()
                print(f"Message from {client_name}: {message}")  # Debug nội dung tin nhắn
                broadcast_message(f"{client_name}: {message}", client_socket)

            elif message_type == "FILE":
                file_name = client_socket.recv(1024).decode()
                file_size = int(client_socket.recv(1024).decode())
                file_data = client_socket.recv(file_size)

                # Lưu file vào server
                server_files[file_name] = file_data
                print(f"Received file '{file_name}' from {client_name}, size: {file_size} bytes")
                broadcast_file(file_data, file_name, client_socket)

            elif message_type == "REQUEST_FILE":
                requested_file = client_socket.recv(1024).decode()
                if requested_file in server_files:
                    file_data = server_files[requested_file]
                    client_socket.sendall(f"FILE_DOWNLOAD\n{requested_file}\n{len(file_data)}".encode())
                    client_socket.sendall(file_data)
                    print(f"Sent file '{requested_file}' to {client_name}")
    except Exception as e:
        print(f"Error with client {client_name}: {e}")
    finally:
        # Client ngắt kết nối
        clients.pop(client_socket)
        broadcast_message(f"{client_name} has left the chat", None)
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.189', 12344))
    server_socket.listen()

    print("Chat server started...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_name = f"Client{len(clients) + 1}"
        clients[client_socket] = client_name
        print(f"{client_name} connected from {client_address}")

        broadcast_message(f"{client_name} has joined the chat")
        threading.Thread(target=handle_client, args=(client_socket, client_name)).start()

if __name__ == "__main__":
    start_server()
