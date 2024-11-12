class user:
    def __init__(self, username, socket, role, alive=True):
        self.username = username
        self.socket = socket
        self.role = role
        self.alive = alive
