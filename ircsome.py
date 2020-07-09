from protocol import protocol_manager as pm
import os
# Port and ip
# TODO: make these changable
server_ip = '127.0.0.1'# input("Server ip? ")
port = 6667 # int(input("Server port? ")) # irc port
# don't ask why, lets me have colored text
os.system('')
print("\x1b[31m!!~~~~~~~~~~~~~~~~~~~~Welcome to IRCsome~~~~~~~~~~~~~~~~~~~~!!\x1b[0m")
print("          \x1b[34mA simple irc client for your command line!          ")
print("    version 1.0.0. made by pawnlord (github.com/pawnlord).         ")
print("  First, input some important information needed to register  \x1b[0m")
# Needed to register
PASS = input("\x1b[33mPassword?\x1b[0m ")
NICK = input("\x1b[33mNickname?\x1b[0m ")
USERNAME = input("\x1b[33mUsername?\x1b[0m ")
REALNAME = input("\x1b[33mRealname?\x1b[0m ") 

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
        msg = input( "\x1b[34m<" + NICK + ">\x1b[32m (" + manager.channel + "):\x1b[0m ")
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