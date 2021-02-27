import socket
import json
from threading import Thread
import time
from person import Person

users = []

HOST = '127.0.0.1'
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)


def client_communication(client, addr):
    global users
    run = True
    person = Person(addr=addr, conn=client)
    login_message = 'Введите логин'.encode('utf8')
    person.conn.send(login_message)
    person.name = person.conn.recv(BUFSIZE).decode('utf8')
    person.conn.send(f'Вы залогинились как {person.name}'.encode('utf8'))
    if person not in users:
        users.append(person)
    while run:
        try:
            data = person.conn.recv(BUFSIZE).decode('utf8')
        except:
            print(f'Пользователь {person.name} {person.addr} отключился')
            users.remove(person)
            break
        response = (person.name + ':' + data).encode('utf8')
        for user in users:
            if user != person:
                try:
                    user.conn.send(response)
                except:
                    del user 

def accept_connections():
    SERVER.listen(10)
    run = True
    while run:
        try:
            conn, addr = SERVER.accept()
            print(f'Пользователь {addr} подключился')
            t = Thread(target=client_communication, args=(conn, addr))
            t.start()
        except Exception as e:
            print('[Fail]', e)
            run = False




if __name__ == "__main__":
    accept_connections()
    