import socket
import threading
from requests import get


def GetIP():
    ip = get('https://api.ipify.org').text
    return ip


GetIP()

HOST = GetIP()
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients=[]
nicknames = []

# broadcast

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]}")
            broadcast(message)
        except:
            index = clients.index(client)
            client.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def recive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("Nick".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server\n".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client))


print("Server running")
recive()