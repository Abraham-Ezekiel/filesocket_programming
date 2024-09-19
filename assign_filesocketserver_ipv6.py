#!/usr/bin/env python3
import socket as S

def start_tcp_server():
    server_socket = S.socket(S.AF_INET6, S.SOCK_STREAM)

    # Use the link-local address with the correct scope ID
    addr_info = S.getaddrinfo('fe80::9d6f:bd1a:a3f8:429b%wlan0', 8080, S.AF_INET6, S.SOCK_STREAM)
    server_socket.bind(addr_info[0][4])
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
