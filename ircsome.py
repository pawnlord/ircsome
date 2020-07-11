from protocol import protocol_manager as pm
import os
import config_manager as cm
import sys

cfg = cm.config("default.cfg")

# Port and ip
server_ip = cfg.get_point("DEFAULT_IP", default=["127.0.0.1"])[0] # input("Server ip? ")
port = int(cfg.get_point("DEFAULT_PORT", default=["6667"])[0]) # int(input("Server port? ")) # irc port

for i in range(len(sys.argv)):
    if sys.argv[i] == '-p':
        i+=1
        if i >= len(sys.argv):
            print('ircsome: -p needs port!')
            exit()
        port = int(sys.argv[i])
    if sys.argv[i] == '-a':
        i+=1
        if i >= len(sys.argv):
            print('ircsome: -a needs address!')
            exit()
        server_ip = sys.argv[i]

print(port, type(port))
print(server_ip, type(server_ip))

COLORS = {"RED" : "\x1b[31m",
"BLUE" : "\x1b[34m",
"YELLOW" : "\x1b[32m",
"LIGHT_BLUE" : "\x1b[36m",
"PURPLE" : "\x1b[35m",
"ORANGE" : "\x1b[33m",
"NONE" : "\x1b[0m"}

# get config file data
title_clr = COLORS[cfg.get_point("TITLE_COLOR", default=["NONE"])[0]]
body_clr = COLORS[cfg.get_point("BODY_COLOR", default=["NONE"])[0]]
input_clr = COLORS[cfg.get_point("INPUT_COLOR", default=["NONE"])[0]]

name_clr = COLORS[cfg.get_point("NAME_COLOR", default=["NONE"])[0]]
text_clr = COLORS[cfg.get_point("TEXT_COLOR", default=["NONE"])[0]]
channel_clr = COLORS[cfg.get_point("CHANNEL_COLOR", default=["NONE"])[0]]


cmd_str = cfg.get_point("CMD_STR", default=["!"])[0]
pm_str = cfg.get_point("PM_STR", default=["@"])[0]

clear_clr =  "\x1b[0m"


# don't ask why, lets me have colored text
os.system('')
print(title_clr +"!!~~~~~~~~~~~~~~~~~~~~Welcome to IRCsome~~~~~~~~~~~~~~~~~~~~!!" + clear_clr)
print(body_clr + "          A simple irc client for your command line!          ")
print("    version 1.0.0. made by pawnlord (github.com/pawnlord).         ")
print("  First, input some important information needed to register  " + clear_clr)
# Needed to register
PASS = input(input_clr + "Password? " + clear_clr)
NICK = input(input_clr + "Nickname? " + clear_clr)
USERNAME = input(input_clr + "Username? " + clear_clr)
REALNAME = input(input_clr + "Realname?\x1b[0m " + clear_clr) 

# Manages protocol
manager = pm.protocol_manager(server_ip, port, PASS, NICK, USERNAME, REALNAME, name_clr, text_clr, cmd_str, pm_str)

i = 0
# main function
def main():
    running = True
    # get any message in the buffer
    manager.get_message(2048)

    # try to get input. If there's a Keyboard interrupt, quit
    try:
        msg = input( name_clr + "<" + NICK + ">" + channel_clr + " (" + manager.channel + "): " + clear_clr)
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