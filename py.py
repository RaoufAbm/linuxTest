import tkinter as tk
import socket
import threading
from PIL import Image, ImageTk  # Import both Image and ImageTk from PIL

# Rest of your code...


def imagPath(argument):
    switcher = {
        "1": "img/info.png",
        "2": "img/ok.png",
        "3": "img/err.png",
        "4": "img/ave.png",
    }
    return switcher.get(argument)

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

            tailleimg = int(parts[7]) * 50
            labelMsg.place(x=10, y=tailleimg + 50)

            image_path = imagPath(parts[0]) 
            image = Image.open(image_path)
            image = image.resize((tailleimg, tailleimg))  
            photo = ImageTk.PhotoImage(image)
            label_image.configure(image=photo)
            label_image.image = photo

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

image_path = "img/info.png" 
image = Image.open(image_path)
image = image.resize((50, 50)) 
photo = ImageTk.PhotoImage(image)

label_image = tk.Label(root, image=photo)
label_image.pack(padx=10, pady=10, anchor="nw", side="top")  

root.attributes("-fullscreen", True)  # For Linux systems
root.mainloop()

