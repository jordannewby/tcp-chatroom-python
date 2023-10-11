import threading
import socket

host = '127.0.0.1'
port = 59960

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients =[]
names = []

def broadcast(message):
    for client in clients:
        client.send(message)

#Function to handle clients connection
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = names[index]
            broadcast('f{nickname} has disconnected'.encode('utf-8'))
            names.remove(nickname)
            break

# Function to recieve the clients connection 
def receive():
    while True:
        print('Server listening and running')
        client , address = server.accept()
        print(f'Connection is being established with {str(address)}')
        client.send('name?'.encode('utf-8'))
        name = client.recv(1024)
        names.append(name)
        clients.append(client)
        print(f'The name of this client is {name}'.encode('utf-8'))
        broadcast(f'{name} has connected to the room'.encode('utf-8'))
        client.send('You are not connected!'.encode('utf-8'))

        thread = threading.Thread(target = handle_client, args=(client,))
        thread.start()

if __name__  == "__main__":
    receive()