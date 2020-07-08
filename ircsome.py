from protocol import protocol_manager as pm
server_ip = '127.0.0.1'# input("Server ip? ")
port = 6667 # int(input("Server port? ")) # irc port

PASS = input("Password? ") + '\r\n'
NICK = input("Nickname? ") + '\r\n'
USERNAME = input("Username? ")
REALNAME = input("Realname? ") + '\r\n'

manager = pm.protocol_manager(server_ip, port, PASS, NICK, USERNAME, REALNAME)

i = 0
channel = ""
def main():
    global channel
    running = True
    manager.get_message(2048)

    try:
        msg = input("send (" + manager.channel + "): ")
    except KeyboardInterrupt:
        msg = "!QUIT"
        running = False

    manager.send_message(msg)
    
    return running

if __name__ == "__main__":
    running = True
    while running:
        running = main()