import socket
s = socket.socket()
server_ip = '127.0.0.1'# input("Server ip? ")
port = 6667 # int(input("Server port? ")) # irc port

PASS = input("Password? ") + '\r\n'
NICK = input("Nickname? ") + '\r\n'
USERNAME = input("Username? ")
REALNAME = input("Realname? ") + '\r\n'

s.connect((server_ip, port))
s.settimeout(1.0)


# try twice, sometimes takes that long
for i in [0, 1]:
    try:
        print(s.recv(1024).decode(), end='')
    except socket.timeout:
        print("Timeout detected, moving on");

s.send(("PASS " + PASS).encode('utf-8'))
try:
    print(s.recv(1024).decode(), end='')
except socket.timeout:
    print("Timeout detected, moving on");

print("PASS SENT")

s.send(("NICK " + NICK).encode('utf-8'))
try:
    returned = s.recv(1024).decode() 
    print(returned, end='')
    s.send(("PONG" + returned[len("PONG"):]).encode('utf-8'))
except socket.timeout:
    print("Timeout detected, moving on");


s.send(("USER " + USERNAME + " 0 * :" + REALNAME).encode('utf-8'))
try:
    print(s.recv(1024).decode(), end='')
except socket.timeout:
    print("Timeout detected, moving on");


i = 0
channel = ""
def main():
    global channel
    running = True
    try:
        print(s.recv(10240).decode(), end='')
    except socket.timeout:
        print("Timeout detected, moving on");
    
    try:
        msg = input("send?")
        if not len(msg) == 0:
            if msg[:4] == "JOIN":
                channel = msg[5:]
            elif msg[0] == '!':
                msg = msg[1:]
            else:
                msg = "PRIVMSG " + channel + " " + msg

    except KeyboardInterrupt:
        msg = "QUIT"
        running = False
    s.send((msg + '\r\n').encode('utf-8'))
    
    return running

if __name__ == "__main__":
    running = True
    while running:
        running = main()