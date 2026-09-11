users = {}

def register(username, password):
    users[username] = password
    return "Registration successful"

def login(username, password):
    if username in users and users[username] == password:
        return "Login successful"
    return "Invalid login"
