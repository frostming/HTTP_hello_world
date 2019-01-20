import socket
import asyncio


async def handle_request(client, loop):
    await loop.sock_sendall(client, b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 11\r\n\r\nhello world\r\n")
    client.close()


async def run_server(loop):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('localhost', 8003))
        server.listen()
        server.setblocking(False)
        print("start listening...")
        while True:
            try:
                client, _ = await loop.sock_accept(server)
                loop.create_task(handle_request(client, loop))
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_server(loop))
