import socket
s = socket.socket()
server_ip = input("Server ip? ")
port = int(input("Server port? ")) # irc port

s.connect((server_ip, port))
s.settimeout(5.0)
i = 0
def main():
    try:
        print(s.recv(1024).decode())
    except socket.timeout:
        print("Timeout detected, moving on");
    s.send((input("send?") + '\r\n').encode('utf-8'))
    return True

if __name__ == "__main__":
    running = True
    while running:
        running = main()