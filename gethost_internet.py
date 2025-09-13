import socket

def get_host():
    s = socket.socket()
    domain = 'www.openai.com'
    ip = socket.gethostbyname(domain)
    print(f"A {domain} domain IP címe: {ip}.")
