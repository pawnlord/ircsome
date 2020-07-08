import socket



class protocol_manager:
    def __init__(self, ip, port, PASS, NICK, USERNAME, REALNAME):
        self.s = socket.socket()

        self.s.connect((ip, port))
        self.s.settimeout(1.0)


        # try twice, sometimes takes that long
        for i in [0, 1]:
            self.get_message(10240)

        self.s.send(("PASS " + PASS).encode('utf-8'))
        self.get_message(1024)
        
        self.s.send(("NICK " + NICK).encode('utf-8'))
        try:
            returned = self.s.recv(1024).decode() 
            print(returned, end='')
            self.s.send(("PONG" + returned[len("PONG"):]).encode('utf-8'))
        except socket.timeout:
            print("Timeout detected, moving on");


        self.s.send(("USER " + USERNAME + " 0 * :" + REALNAME).encode('utf-8'))
        self.get_message(20480)

        self.channel = ""
    
    def send_message(self, msg):
        if len(msg) > 0:
            if msg[:5].lower() == "!join":
                self.channel = msg[6:]
            elif msg[0] == '!':
                msg = msg[1:]
            else:
                if self.channel == "":
                    print("ircsome: Not in a channel! use !join <channel> to join one!")
                    return
                msg = "PRIVMSG " + self.channel + " " + msg
        self.s.send((msg + '\r\n').encode('utf-8'))
    
    def get_message(self, size):
        try:
            print(self.s.recv(size).decode(), end='')
        except socket.timeout:
            pass
