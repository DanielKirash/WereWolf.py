import socket
import threading

# Server configuration
HOST = 'localhost'
PORT = 12345

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to server")
    thread = threading.Thread(target=recv_message, args=(client_socket,))
    thread.start()

def recv_message(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            print("Received:", message)

            if 'Choose your username' in message:
                username = input("Enter your username: ")
                client_socket.sendall(username.encode())
            elif 'Choose' in message:
                response = input(message)
                client_socket.sendall(response.encode())

    except Exception as e:
        print("Error:", e)

# Start the client
start_client()
