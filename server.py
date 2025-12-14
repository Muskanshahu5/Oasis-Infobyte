import socket
import threading

host = "127.0.0.1"
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

print("Server started...")
print("Waiting for clients...")

while True:
    client, address = server.accept()
    print(f"Connected with {address}")
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
