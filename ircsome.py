from protocol import protocol_manager as pm
# Port and ip
# TODO: make these changable
server_ip = '127.0.0.1'# input("Server ip? ")
port = 6667 # int(input("Server port? ")) # irc port

# Needed to register
PASS = input("Password? ")
NICK = input("Nickname? ")
USERNAME = input("Username? ")
REALNAME = input("Realname? ") 

# Manages protocol
manager = pm.protocol_manager(server_ip, port, PASS, NICK, USERNAME, REALNAME)

i = 0
# main function
def main():
    running = True
    # get any message in the buffer
    manager.get_message(2048)

    # try to get input. If there's a Keyboard interrupt, quit
    try:
        msg = input( "<" + NICK + "> (" + manager.channel + "): ")
    except KeyboardInterrupt:
        msg = "!QUIT"
        running = False

    manager.send_message(msg, format=True)
    if msg.lower() == "!quit":
        running = False

    return running


if __name__ == "__main__":
    # tells if we stopped
    running = True
    # main loop
    while running:
        running = main()