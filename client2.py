import socket

HOST="127.0.0.1"
SERVER_PORT=65431

FORMAT="utf8"


        
        
        

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