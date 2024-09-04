import socket

HOST="127.0.0.1"
SERVER_PORT=65431

FORMAT="utf8"


        
def DisplayMenu(conn:socket){
    print("Chon dang nhap hoac dang ky")
    print("Nhap login de dang nhap")
    print("Nhap register de dang ky")
}       


def Register(conn:socket):
    
def Login(conn:socket):
    # DJoiwajd

def sendUserInfor(client, list):
    
    listUserInfor=list
    msg="login"
    client.sendall(msg.encode(FORMAT))
    client.recv(1024)

    for x in listUserInfor:
        client.sendall(x.encode(FORMAT))
        client.recv(1024)
    msg="end"
    client.sendall(msg.encode(FORMAT))
    msg=client.recv(1024).decode(FORMAT)
   
    
    if(msg=="ok"):
        print("Thanh cong")
        
        
    msg= client.recv(1024).decode(FORMAT)
    
    if(msg=="Register"):
        
        msg=input("Vui long dang Ky, vui long nhap chu dangky de dang ky" )

        client.sendall(msg.encode(FORMAT))
        
        
        
        username=input("Vui long dang Ky, vui long nhap chu dangky de dang ky" )
        password=input("Nhap password")
        
 

   
    

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Client Side")
try:

    client.connect((HOST,SERVER_PORT))
    print("Client address",client.getsockname())
    




    msg= None
    list=[]
    while(msg!= "x"):
   
        
        username=input("Nhap user name: ")
        list.append(username)
        password=input("Nhap mat khai: ")
        list.append(password)

        
     
        sendUserInfor(client, list)

except:
    print("Error")

input()