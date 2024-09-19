#!/usr/bin/env python3
import socket as S

def start_tcp_server():
    server_socket = S.socket(S.AF_INET, S.SOCK_STREAM)

    # Bind to the IPv4 address and port
    server_socket.bind(('192.168.43.200', 8080))  # Listen on all available interfaces
    server_socket.listen(5)
    print("TCP Server listening on port 8080")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Get the file name to send from the user
        file_path = input("Enter the name of the file to send: ")

        try:
            with open(file_path, 'rb') as f:
                print("Sending file...")
                while chunk := f.read(1024):
                    client_socket.sendall(chunk)
                print("File sent successfully")
        except FileNotFoundError:
            print(f"File {file_path} not found")

        client_socket.close()

if __name__ == "__main__":
    start_tcp_server()
