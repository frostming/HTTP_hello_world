import socket
from threading import Thread


def handle_request(client):
    client.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 11\r\n\r\nhello world\r\n")
    client.close()


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('localhost', 8002))
        server.listen()
        print("start listening...")
        while True:
            try:
                client, _ = server.accept()
                Thread(target=handle_request, args=(client,)).start()
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    run_server()
