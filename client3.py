import socket

clientSocket = socket.socket()

host = "127.0.0.1"
port = 9090
clientSocket.connect((host, port))

data = input(' -> ')
while data.strip().lower() != 'bye':
    # küldök üzenetet
    clientSocket.send(data.encode())
    # fogadom az üzenetet
    dataFromServer = clientSocket.recv(1024).decode()
    print("Szerver üzenete: ", dataFromServer)
    # újra bekérek...
    data = input(' -> ')
# clientSocket.close()