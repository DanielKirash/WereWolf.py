#Wolf turn handler
def handle_wolf_turn(wolfs, alive_players, data):
    choices = []
    for wolf in wolfs:
        wolf.socket.send(data.encode())
        wolf.socket.send('Wolfs wake up. Choose a player to kill:'.encode())
        while True:
            choice = wolf.socket.recv(1024).decode()
            if choice in alive_players:
                choices.append(choice)
                break
            else:
                wolf.socket.sendall('Invalid choice. Choose a player to kill:'.encode())
    return choices

#Seer turn handler
def handle_seer_turn(seers, alive_players, data):
    choices = []
    for seer in seers:
        seer.socket.sendall(data.encode())
        seer.socket.sendall('Seer wake up. Choose a player to see:'.encode())
        while True:
            choice = seer.socket.recv(1024).decode()
            if choice in alive_players:
                choices.append(choice)
                break
            else:
                seer.socket.sendall('Invalid choice. Choose a player to see:'.encode())
    return choices

#Medium turn handler
def handle_medium_turn(mediums, dead_players):
    choice = None
    for medium in mediums:
        medium.socket.sendall('Medium wake up. Choose a player to see:'.encode())
        while True:
            choice = medium.socket.recv(1024).decode()
            if choice in dead_players:
                return choice
            else:
                medium.socket.sendall('Invalid choice. Choose a player to see:'.encode())

#Chavalry turn handler
def handle_chavalry_turn(chavalries, alive_players, data):
    choice = []
    for chavalry in chavalries:
        chavalry.socket.sendall(data.encode())
        chavalry.socket.sendall('Chavalry wake up. Choose a player to protect:'.encode())
        while True:
            choice = chavalry.socket.recv(1024).decode()
            if choice in alive_players:
                return choice
            else:
                chavalry.socket.sendall('Invalid choice. Choose a player to protect:'.encode())
       