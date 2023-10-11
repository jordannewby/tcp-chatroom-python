import threading
import socket

name = input('Choose a name: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59960))

def receive_message():
  while True:
    try:
      message = client.recv(1024).decode('utf-8')
      if message == "name?":
        client.send(name.encode('utf-8'))
      else:
        print(message)
    except:
     print('Error')
     client.close()
     break

def send_message():
  while True:
    message = f'{name}: {input("")}'
    client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target= receive_message)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()