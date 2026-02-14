# client.py
import socket
import threading

HOST = '127.0.0.1'   # Change if using different system
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

name = input("Enter your name: ")

# Receive messages
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == "NAME":
                client_socket.send(name.encode())
            else:
                print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

# Send messages
def send_messages():
    while True:
        message = input("")
        full_message = f"{name}: {message}"
        client_socket.send(full_message.encode())

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
