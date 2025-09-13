import socket

clientSocket = socket.socket()

host = "127.0.0.1"
port = 9090
clientSocket.connect((host, port))
data = input('Neved: ')
while data.strip().lower() != 'bye':
    clientSocket.send(data.encode())
    dataFromServer = clientSocket.recv(1024).decode()
    print("Szerver üzenete: ", dataFromServer)
    if(dataFromServer.__contains__('!')):
        clientSocket.send('Velem te így ne beszélj!!!!! SZÉP NAPOT!!!'.encode())
        clientSocket.close()
    if(dataFromServer.__contains__("@")):
        print("A kapcsolat megszűnt a szerverrel.")
        clientSocket.close()
        break
    else:
        data = input(' -> ')
clientSocket.close()