import socket

HEADER = 64
PORT = 30001
FORMAT = 'utf-8'
DISCONNECTED_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = "172.17.0.5"
# SERVER = ""    put your public ip address to connect to the server over the internet
ADDR = ("192.168.49.2", PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello Friend!")
