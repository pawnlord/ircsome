import socket



class protocol_manager:
    def __init__(self, ip, port, PASS, NICK, USERNAME, REALNAME):
        self.s = socket.socket()

        self.s.connect((ip, port))
        self.s.settimeout(1.0)


        self.channel = ""
    
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
                    self.channel = msg.split(' ')[1]
                pass
            else:
                if msg[:5].lower() == "!join":
                    self.channel = msg[6:]
                if msg[0] == '!':
                    msg = msg[1:]
                else:
                    msg = "PRIVMSG " + self.channel + " " + msg
        print("sending message " + msg)
        self.s.send((msg + '\r\n').encode('utf-8'))
    
    def get_message(self, size):
        try:
            msg = self.s.recv(size).decode()
            if "PING" in msg:
                print("PING FOUND")
                return_msg = "PONG :" + msg.split(':')[1].split('\r')[0]
                self.send_message(return_msg)
            print(msg, end='')
        except socket.timeout:
            pass
