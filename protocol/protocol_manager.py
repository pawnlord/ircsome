import socket


# Manages any protocol commands (PRIVMSG, JOIN, PING/PONG)
class protocol_manager:
    def __init__(self, ip, port, PASS, NICK, USERNAME, REALNAME, name_clr, text_clr, cmd_str, pm_str):
        # socket
        self.s = socket.socket()

        # connect to ip
        self.s.connect((ip, port))
        # timeout
        self.s.settimeout(1.0)

        # Channel that we send to
        self.channel = ""
        # If join fails, we fall back to the last one
        self.last_channel = ""
    
        # try twice, sometimes takes that long
        for i in [0, 1]:
            self.get_message(10240)

        # Register account

        # password
        self.send_message("PASS " + PASS, format=False)
        self.get_message(1024)
        
        # nickname
        self.send_message("NICK " + NICK, format=False)
        self.get_message(1024)

        # username and realname
        self.send_message("USER " + USERNAME + " 0 * :" + REALNAME, format=False)
        self.get_message(20480)

        self.name_clr = name_clr
        self.text_clr = text_clr
        
        self.cmd_str = cmd_str
        self.pm_str = pm_str

    def send_message(self, msg, format):
        # some messages are just commands
        if format:
            # If there isn't anything, don't risk checking it
            if len(msg) > 0:
                # if there isn't a channel, still check for a join
                if self.channel == "":
                    if msg[:len(self.cmd_str)+len("join")].lower() == self.cmd_str + "join" or msg[:len("join")].lower() == "join" :
                        self.last_channel = self.channel
                        self.channel = msg.split(' ')[1]
                    
                else: # Main formatting
                    # get channel we joined
                    if msg[:len(self.cmd_str)+len("join")].lower() == self.cmd_str + "join":
                        self.last_channel = self.channel
                        self.channel = msg[6:]
                    # special character to send a normal message
                    if msg[:len(self.cmd_str)] == self.cmd_str:
                        msg = msg[len(self.cmd_str):]
                    elif msg[:len(self.pm_str)] == self.pm_str: # send a pm to someone
                        msg = "PRIVMSG " + msg[len(self.pm_str):]
                    else: # send message to channel
                        msg = "PRIVMSG " + self.channel + " " + msg
        # send message in a way it's acceptable
        self.s.send((msg + '\r\n').encode('utf-8'))
    
    def get_message(self, size):
        # try to get the message
        try:
            # get message
            msg = self.s.recv(size).decode()
            # deal with PINGS
            if "PING" in msg:
                return_msg = "PONG :" + msg.split(':')[1].split('\r')[0]
                self.send_message(return_msg, format=False)
                return
            # deal with any info
            info = msg.split(':')[1]
            # revert channel if we need to
            if "448" in info: 
                self.channel = self.last_channel
            # format a normal message
            user = ""
            if '!' in msg and not '001' in msg:
                user = msg.split('!')[0][1:]
                msg = self.name_clr + "<{}>:{} ".format(user, self.text_clr) + msg.split(':')[2]
            
            # add a eol to a message that doesn't have it
            if msg[-1] != '\n':
                msg+='\n'
            msg += "\x1b[0m"
            # output message
            print(msg, end='')
        except socket.timeout:
            # if we timeout, that's fine
            pass
