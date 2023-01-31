import socket
import threading
import hashlib

from cryptography.fernet import Fernet

choose=input("Do you want to host(1) or connect(2)?")
if choose=="1":
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen()
    client, _ = server.accept()
   
elif choose=="2":
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("0.0.0.0" , 8080))
  
else:
    exit()

def sendingmessages(c):
    passwd = input("Enter password for encrypted chat : ") 
    while True:
        print(decrypt(passwd,client.recv(1024)).decode('utf-8'))
        message=input("Enter your text here:")
        encMessage = hashlib.sha512(message.encode())
        encMsg = encrypt(passwd,("You:"+ message))
        client.send(encMessage)
      

def recievemessages(c):
        while True:
            print("Them:"+ client.recv(1024).decode())

threading.Thread(target=sendingmessages, args=(client,)).start()
threading.Thread(target=recievemessages, args=(client,)).start()
