import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(1)

print('Listening on port %s ...' % SERVER_PORT)

while True:
    connectionSocket, address = serverSocket.accept()

    message = connectionSocket.recv(1024).decode()
    print(message)

    file = message.split()[1]

    try:
        f = open(file[1:])
        content = f.read()
        f.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
        
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\n404 Not Found'

    connectionSocket.sendall(response.encode())
    connectionSocket.close()