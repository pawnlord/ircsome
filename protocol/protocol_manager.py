import socket



class protocol_manager:
    def __init__(self, ip, port, PASS, NICK, USERNAME, REALNAME):
        self.s = socket.socket()

        self.s.connect((ip, port))
        self.s.settimeout(1.0)


        self.channel = ""
        self.last_channel = ""
    
        # try twice, sometimes takes that long
        for i in [0, 1]:
            self.get_message(10240)

        self.s.send(("PASS " + PASS).encode('utf-8'))
        self.get_message(1024)
        
        self.s.send(("NICK " + NICK).encode('utf-8'))
        self.get_message(1024)


        self.s.send(("USER " + USERNAME + " 0 * :" + REALNAME).encode('utf-8'))
        self.get_message(20480)
    def send_message(self, msg):
        if len(msg) > 0:
            if self.channel == "":
                if msg[:5].lower() == "!join" or msg[:4].lower() == "join" :
                    self.last_channel = self.channel
                    self.channel = msg.split(' ')[1]
                pass
            else:
                if msg[:5].lower() == "!join":
                    self.last_channel = self.channel
                    self.channel = msg[6:]
                if msg[0] == '!':
                    msg = msg[1:]
                elif msg[0] == '@':
                    msg = "PRIVMSG " + msg[1:]
                else:
                    msg = "PRIVMSG " + self.channel + " " + msg
        self.s.send((msg + '\r\n').encode('utf-8'))
    
    def get_message(self, size):
        try:
            msg = self.s.recv(size).decode()
            if "PING" in msg:
                return_msg = "PONG :" + msg.split(':')[1].split('\r')[0]
                self.send_message(return_msg)
            info = msg.split(':')[1]
            if "448" in info:
                self.channel = self.last_channel
            user = ""
            if '!' in msg and not '001' in msg:
                user = msg.split('!')[0][1:]
                msg = "<{}>: ".format(user) + msg.split(':')[2]
            print(msg, end='')
        except socket.timeout:
            pass
