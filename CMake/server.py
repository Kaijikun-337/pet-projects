import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
print(f'Starting server on {server_address}...')
sock.bind(server_address)
sock.listen(1)

while True:
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    try:
        print(f'Connection from {client_address}')
        while True:
            data = connection.recv(1024)
            if data:
                print(f'Received: "{data.decode()}"')
                connection.sendall(b'Ack: ' + data) # Reply
            else:
                break
    finally:
        connection.close()