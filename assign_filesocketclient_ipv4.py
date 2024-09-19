#!/usr/bin/env python3
import socket as S

def start_tcp_client():
    client_socket = S.socket(S.AF_INET, S.SOCK_STREAM)

    # Connect to the IPv4 address and port of the server
    client_socket.connect(('server_ip_address', 8080))  # Replace 'server_ip_address' with the actual IP

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
