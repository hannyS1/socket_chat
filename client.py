import socket
import json
from threading import Thread



def run():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8000))
    t1 = Thread(target=send_message, args=(client_socket, ))
    t2 = Thread(target=take_data, args=(client_socket, ))
    t1.start()
    t2.start()
        
        
def send_message(conn):
    while True:
        
        message = str(input())
        conn.send(message.encode())

def take_data(conn):
    while True:
        data = conn.recv(1024).decode()
        print(data)
    

    
if __name__ == "__main__":
    run()