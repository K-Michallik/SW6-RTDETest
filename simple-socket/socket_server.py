import socket
import logging

HOST = '0.0.0.0'
PORT = 55555
pose = '(-0.15,-0.5,0.3,0,-3.14,0)'
response = 'world'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, address = s.accept()
    with conn:
        print('Connected by[print] ', address)
        # logging.warning('Connected by[log warning] ' + address)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if "hello" in str(data):
                conn.sendall(response.encode())
                print('Data sent.')
