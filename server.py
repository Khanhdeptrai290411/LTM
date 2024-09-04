import socket
import threading
import database

HOST="127.0.0.1"
SERVER_PORT=65431
FORMAT="utf8"



def checkAccount(username, passwd ):
    
    if(database.checkUser(username,passwd)):
        return True
    else: 
        return False
    
def handleClient(conn : socket,addr):
   
    print("conn", conn.getsockname())
    
    msg= None
    ListRec=[]
    while(msg!= "x"):
        msg=conn.recv(1024).decode(FORMAT)
        if(msg=='login'):
            msg="success"
            conn.sendall(msg.encode(FORMAT))
            msg=conn.recv(1024).decode(FORMAT)

            while(msg!='end'):
                
                ListRec.append(msg)
                conn.sendall(msg.encode(FORMAT))
                msg=conn.recv(1024).decode(FORMAT)


            msg="ok"
            conn.sendall(msg.encode(FORMAT))
            
            username=ListRec[0]
            passwd=ListRec[1]
            msg=checkAccount(username,passwd)
            if(checkAccount(username,passwd)):
                print("Dang nhap thanh cong")
            else: print("Dang nhap that bai")    
                
            
        elif(msg=='register'):
            msg="success"
            conn.sendall(msg.encode(FORMAT))
            msg=conn.recv(1024).decode(FORMAT)

            while(msg!='end'):
                
                ListRec.append(msg)
                conn.sendall(msg.encode(FORMAT))
                msg=conn.recv(1024).decode(FORMAT)


            msg="ok"
            conn.sendall(msg.encode(FORMAT))

            
            
            
        
        
      
            
            
            




             
             
      

           
        
   
    conn.getsockname()
    conn.close()   
        




s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,SERVER_PORT))
s.listen()

print("SERVER SIDE")

print("Server:" , HOST, SERVER_PORT)
print("Waiting client")




clientNumber=0
try:
    while(clientNumber<3):
        conn, addr= s.accept()
        thr= threading.Thread(target=handleClient,args=(conn,addr))
        thr.daemon=True
        thr.start()

        clientNumber+=1
        
    
    
  

except:
    print("Error")
    s.close()
    










