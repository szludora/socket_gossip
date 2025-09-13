import socket
import random
import os


def connection(server_socket):
    client_connected, client_address = server_socket.accept()
    os.system('cls')
    print("*************************************")
    print(f"Üdvözöllek {client_address[0]}(localhost) : {client_address[1]} (port szám)!")
    return client_connected, client_address[1]


def server_program():
    server_socket = socket.socket()         # Create a socket object
    host = '127.0.0.1'                      # localhost
    port = 9090                             # 1023-nál nagyobb szám
    server_socket.bind((host, port))        # kapcsolás a porthoz (tuple a bemenet)
    server_socket.listen(5)                 # Now wait for client connection.
    news_updated = []       # legfrissebb hírek összesítve
    news = []               # hírek - gyűjtés alatt
    gossip = False          # az elején még nem pletykálunk
    random_gossip = ""      # az elején még nincs mit...
    # felvesszük a kapcsolatot a klienssel
    client_connected, port_kliens = connection(server_socket)
    living_connection = True
    while living_connection:
        # ha már pletyizhetek
        if gossip:
            ...
            # kiválasztok egy véletlen indexet (*)
            # előző kliensektől kis pletyi, azaz a véletlen index alapján választunk hírt (*)
        # fogadom a kliens üzenetét
        data_from_client = client_connected.recv(1024).decode()
        # ha kapok üzenetet...
        if data_from_client:
            # begyűjtöm a friss pletyit (*)
            # összerakom a kliens üzenetét a friss pletyivel együtt
            data = input(" -> ") + random_gossip
            # üzenet küldése a kliensnek
            client_connected.send(data.encode())
        # amikor a kliens elköszönt (bye)
        else:
            # kapcsolódok az új klienshez
            client_connected, port_kliens = connection(server_socket)
            # most már pletyizhetek (*)
            # új pletyiket frissítem, azaz kibővítem a listát a most gyűjtött hírekkel (*)
            