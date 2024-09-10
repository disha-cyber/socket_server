import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port to connect to
server_address = ('localhost', 12346)

# Connect to the server
client_socket.connect(server_address)

while True:
    # Send a message to the server
    message = input("Client: ")
    client_socket.send(message.encode('utf-8'))

    # Receive a response from the server
    response = client_socket.recv(1024)
    print(f"Server says: {response.decode('utf-8')}")

# Close the socket
client_socket.close()
