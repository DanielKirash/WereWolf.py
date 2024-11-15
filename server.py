import socket
import threading
import random
from user import user
import json
from turn_handlers import handle_wolf_turn, handle_seer_turn, handle_medium_turn, handle_chavalry_turn

# Server configuration
HOST = 'localhost'
PORT = 12345

# Lists of connected clients and players
clients = []
players = []

# Roles and role-specific lists
roles = ['wolf', 'wolf', 'seer', 'medium', 'chavalry', 'villager', 'villager', 'villager', 'villager', 'villager']
#roles = ['wolf', 'wolf', 'wolf']
villagers = []
wolfs = []
seers = []
mediums = []
chavalries = []

# Choices for the night actions
WOLF_CHOICE = None
SEER_CHOICE = None
MEDIUM_CHOICE = None
CHAV_CHOICE = None

# List of usernames
usernames = []

# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Server is listening on port", PORT)
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"New connection from {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

# Function to handle each client connection
def handle_client(client_socket):
    global roles
    try:
        # Receive the username
        client_socket.sendall('Welcome to the server! Choose your username:'.encode())
        username = client_socket.recv(1024).decode()
        if not username:
            return

        usernames.append(username)

        # Assign a random role to the player
        rnd_role = random.choice(roles)
        roles.remove(rnd_role)
        new_user = user(username, client_socket, rnd_role)
        players.append(new_user)

        # Add the player to the respective role list
        if rnd_role == 'villager':
            villagers.append(new_user)
        elif rnd_role == 'wolf':
            wolfs.append(new_user)
        elif rnd_role == 'seer':
            seers.append(new_user)
        elif rnd_role == 'medium':
            mediums.append(new_user)
        elif rnd_role == 'chavalry':
            chavalries.append(new_user)

        print(f'Player {username} has joined the game as {rnd_role}')

        # Notify the client of their role
        client_socket.sendall(f'Your role is {rnd_role}'.encode())

        # Start the game if enough players have joined
        if len(players) == 2:
            broadcast_message('The game is starting...')
            game_loop()

    except Exception as e:
        print("Error:", e)
        clients.remove(client_socket)
        client_socket.close()

# Function to broadcast a message to all clients
def broadcast_message(message):
    for client in clients:
        try:
            client.sendall(message.encode())
        except:
            clients.remove(client)

# Game loop function
def game_loop():
    global WOLF_CHOICE, SEER_CHOICE, MEDIUM_CHOICE, CHAV_CHOICE
    while True:
        
        broadcast_message('The game starts now')
        broadcast_message('The night has come, everyone goes to sleep')

        alive_players = [player.username for player in players if player.alive]
        dead_players = [player.username for player in players if not player.alive]
        data = json.dumps(alive_players)
        dead_data = json.dumps(dead_players)

        # Wolfs' turn
        WOLF_CHOICE = handle_wolf_turn(wolfs, alive_players, data)

        # Seer's turn
        SEER_CHOICE = handle_seer_turn(seers, alive_players, data)

        # Medium's turn
        MEDIUM_CHOICE = handle_medium_turn(mediums, dead_players, dead_data)

        # Chavalry's turn
        CHAV_CHOICE = handle_chavalry_turn(chavalries, alive_players, data)

        # Daytime actions
        broadcast_message('The day has come')

        # Resolve actions
        if WOLF_CHOICE == CHAV_CHOICE:
            broadcast_message('The chavalry saved the player!')
        else:
            random_wolf_choice = random.choice(WOLF_CHOICE)
            broadcast_message(f'The player {random_wolf_choice} has died')
            for player in players:
                if player.username == WOLF_CHOICE:
                    player.alive = False

        # Seer's information
        for seer in seers:
            if SEER_CHOICE in [wolf.username for wolf in wolfs]:
                seer.socket.sendall(f'The player {SEER_CHOICE} is a wolf'.encode())
            else:
                seer.socket.sendall(f'The player {SEER_CHOICE} is not a wolf'.encode())
        
        # Medium's information
        for medium in mediums:
            if MEDIUM_CHOICE in [wolf.username for wolf in wolfs]:
                medium.socket.sendall(f'The player {MEDIUM_CHOICE} was a wolf'.encode())
            else:
                medium.socket.sendall(f'The player {MEDIUM_CHOICE} was not a wolf'.encode())
            

            


# Start the server
start_server()
