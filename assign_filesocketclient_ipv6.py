#!/usr/bin/env python3
import socket as S

def start_tcp_client():
    client_socket = S.socket(S.AF_INET6, S.SOCK_STREAM)

    # Use the link-local address with the correct scope ID
    addr_info = S.getaddrinfo('fe80::9d6f:bd1a:a3f8:429b%wlan0', 8080, S.AF_INET6, S.SOCK_STREAM)
    client_socket.connect(addr_info[0][4])

    # Get the file name to save from the user
    file_name = input("Enter the name to save the received file as: ")

    with open(file_name, 'wb') as f:
        print("Receiving file...")
        while True:
            file_data = client_socket.recv(1024)
            if not file_data:
                break
            f.write(file_data)
        print(f"File received and saved as {file_name}")

    client_socket.close()

if __name__ == "__main__":
    start_tcp_client()
