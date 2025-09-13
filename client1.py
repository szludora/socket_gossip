import socket

clientSocket = socket.socket()
host = "127.0.0.1"
port = 9090
clientSocket.connect((host, port))

data = input("Neved: ")

while True:
    clientSocket.send(data.encode())
    dataFromServer = clientSocket.recv(1024).decode()

    if not dataFromServer:  # szerver bezárta a kapcsolatot
        print("A kapcsolat megszűnt a szerverrel.")
        break

    print("Szerver üzenete:", dataFromServer)

    if "!" in dataFromServer: # illetlen üzeneteknél kilépünk
        print("Ez elég illetlen volt, ezért megszakítottuk a beszélgetést...")
        clientSocket.send("@ Velem te így ne beszélj!!!!! SZÉP NAPOT!!!".encode())
        break

    if "@" in dataFromServer or "bye" in dataFromServer:
        print("A kapcsolat megszűnt a szerverrel.")
        break

    data = input("-> ")
    if data == "bye" or "@" in data:
        print("Kilépés...")
        break

clientSocket.close()