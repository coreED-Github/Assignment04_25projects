import socket
import threading

# Server configuration
HOST = 'localhost'
PORT = 5555

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")

    try:
        # Sending a welcome message to the client
        client_socket.sendall(b"Welcome to Pong!")

        while True:
            try:
                player1_y = client_socket.recv(1024).decode()
                if not player1_y:
                    break
                print(f"Player 1 Y Position: {player1_y}")

                player2_y = client_socket.recv(1024).decode()
                if not player2_y:
                    break
                print(f"Player 2 Y Position: {player2_y}")

                client_socket.sendall(player1_y.encode())
                client_socket.sendall(player2_y.encode())
                
            except Exception as e:
                print(f"Error in communication: {e}")
                break

    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)
    print("Server started, waiting for players...")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()
        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == "__main__":
    start_server()