import socket
import threading

# we are creating the header to tells us how many bytes we are receiving from the client
HEADER = 64
PORT = 5050
#SERVER = socket.gethostbyname(socket.gethostname()) #Give the actual ip address of your machine
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECTED_MESSAGE = "!DISCONNECT"

# our protocol is connection-based which is TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f" [NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #Here we define how many bytes we need to receive from the client
        # we are decoding the message from bytes to string with format utf-8
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECTED_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message received.".encode(FORMAT))
    conn.close()

def start(): #handle new connection
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION {threading.activeCount() - 1}")

print("[STARTING] Server is starting... ")
start()