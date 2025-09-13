import socket
import random
import os

def connection(server_socket):
    client_connected, client_address = server_socket.accept()
    os.system('clear')  # MacOS; Windows: 'cls'
    print("_____________________________")
    print(f"Kapcsolódott: {client_address[0]}:{client_address[1]}")
    print("_____________________________")
    return client_connected, client_address[1]

def server_program():
    server_socket = socket.socket()
    host = '127.0.0.1'
    port = 9090
    server_socket.bind((host, port))
    server_socket.listen(5)

    news_from_client = []
    news_for_client = []

    client_connected, port_kliens = connection(server_socket)
    can_gossip = False
    client_name = ""
    living_connection = True

    while living_connection:
        data_from_client = client_connected.recv(1024).decode()

        # Kliens bezárta a kapcsolatot
        if not data_from_client or "@" in data_from_client:
            print("_____________________________")
            print("A kapcsolat megszűnt a klienssel, várakozás...")
            client_name = ""
            can_gossip = True
            news_for_client.extend(news_from_client)
            news_from_client.clear()
            client_connected, port_kliens = connection(server_socket)
            continue

        # Első üzenet = név
        if not client_name:
            client_name = data_from_client
            client_connected.send(f"Szia {client_name}".encode())
            continue

        # Gyűjtjük a hosszabb üzeneteket pletykának
        if len(data_from_client.split()) > 1:
            news_from_client.append(data_from_client)

        print(f"{client_name}: {data_from_client}")
        data = input("-> ")

        # Szerver bezárása szerver kérésére
        if data == "@":
            client_connected.send("@ meguntam, szia".encode())
            client_connected.shutdown(socket.SHUT_RDWR)  # minden irányban lezárjuk
            client_connected.close()                       # majd lezárjuk a socketet
            break

        # Pletyka kiválasztása, eltávolítva a listából
        random_gossip = ""
        if can_gossip and news_for_client:
            random_gossip = news_for_client.pop(
                random.randint(0, len(news_for_client)-1)
            )

        # Üzenet elküldése kliensnek
        client_connected.send(f"{data} {random_gossip}".strip().encode())
        
    print("Szerver bezárása")
