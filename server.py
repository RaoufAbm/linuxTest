import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name
    host = "localhost"
    
    port = 3553  # Reserve a port for your service
    
    try:
        # Bind to the port
        server_socket.bind((host, port))
        
        # Now wait for client connection
        server_socket.listen(5)
        
        print(f"Server listening on {host}:{port}")
        
        while True:
            # Establish connection with client
            
            
            # client_socket, addr = server_socket.accept()
            # print(f"Got connection from {addr}")


            message_ = client_socket.recv(1024).decode('utf-8')
            print("Received message:", message_)
        

        
            client_socket.send("200".encode('ascii'))
            
            # Close the connection with the client
            client_socket.close()
    
    except Exception as e:
        print("Error:", e)
        # Close the server socket

        server_socket.close()

# Start the server
start_server()

