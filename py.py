import tkinter as tk
import socket
import threading

# Rest of your code...



def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "localhost"
    port = 3553
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")
        
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Got connection from {addr}")

            message_ = client_socket.recv(1024).decode('utf-8')
            parts = message_.split("~")
            print(message_)
            labelTitre.config(text=parts[1], font=("Arial", parts[5]), fg=parts[6])
            labelMsg.config(text=parts[2], font=("Arial", parts[3]), fg=parts[4])

            

      
            client_socket.send("200".encode('ascii'))
            client_socket.close()
    
    except Exception as e:
        print("Error:", e)
        server_socket.close()

server_thread = threading.Thread(target=start_server)
server_thread.start()

root = tk.Tk()
root.title("Simple Application")

frame = tk.Frame(root)
frame.pack()

labelTitre = tk.Label(frame, text="titre", font=("Arial", 20))
labelTitre.pack()
labelMsg = tk.Label(root, text="message", font=("Arial", 20), fg="blue")
labelMsg.place(x=10, y=200)



root.attributes("-fullscreen", True)  # For Linux systems
root.mainloop()

