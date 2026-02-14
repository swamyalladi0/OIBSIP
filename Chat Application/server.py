# server.py
import socket
import threading

# Server configuration
HOST = '0.0.0.0'
PORT = 5000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server is running...")
print("Waiting for connections...\n")

clients = []
names = []

# Broadcast message to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                remove_client(client)

# Remove disconnected client
def remove_client(client):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        name = names[index]
        names.remove(name)
        print(f"{name} disconnected.")
        broadcast(f"{name} left the chat.".encode(), client)
        client.close()

# Handle individual client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            remove_client(client)
            break

# Accept multiple clients
while True:
    client_socket, address = server_socket.accept()
    print(f"Connected with {address}")

    client_socket.send("NAME".encode())
    name = client_socket.recv(1024).decode()

    names.append(name)
    clients.append(client_socket)

    print(f"{name} joined the chat!")

    broadcast(f"{name} joined the chat!".encode(), client_socket)

    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
