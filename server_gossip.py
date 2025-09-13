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
    server_socket = socket.socket()       
    host = '127.0.0.1'                    
    port = 9090                           
    server_socket.bind((host, port))      
    server_socket.listen(5)               
    news_actual_from_client = []     
    news_for_actual_client = []  
    gossip = False        
    random_gossip = ""    
    client_connected, port_kliens = connection(server_socket)
    living_connection = True
    actual_client_name = ""
    
    while living_connection:
        if(not actual_client_name):
            data_from_client = client_connected.recv(1024).decode()
            actual_client_name = data_from_client
            client_connected.send(f'Szia {actual_client_name}!'.encode())

        if gossip:
            random_gossip = news_for_actual_client[random.randint(0, len(news_for_actual_client) - 1)]

        data_from_client = client_connected.recv(1024).decode()
        
        if data_from_client:
            news_actual_from_client.append(data_from_client)
            data = input(f"{actual_client_name}: {data_from_client} -> ")
            client_connected.send(f'{data}, {random_gossip}'.encode())

        else:
            actual_client_name = ""
            gossip = True
            news_for_actual_client.extend(news_actual_from_client)
            news_actual_from_client.clear()
            client_connected, port_kliens = connection(server_socket)