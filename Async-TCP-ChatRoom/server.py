import socket
import asyncio


class Server:

    def __init__(self, hostname, port):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((hostname, port))
        self.client_connected = dict()  # client_socket: nickname

    async def start_server(self):

        self.server.listen(5)
        self.server.setblocking(False)
        print("Waiting for new connections...")

    async def broadcast_message(self, source_client, message):

        loop = asyncio.get_event_loop()

        for client in self.client_connected:

            try:
                await loop.sock_sendall(client, f"{self.client_connected[source_client]}: {message}".encode('utf-8'))
            except Exception as e:
                print(f"Error occurred while sending message to {self.client_connected[client]}: {e}")
                self.client_connected.pop(client)
                client.close()

    async def handle_client(self, client, nickname):

        loop = asyncio.get_event_loop()
        while True:
            # message = client.recv(1024).decode('utf-8')
            message = (await loop.sock_recv(client, 1024)).decode('utf-8')
            if not message:
                print(f"{self.client_connected[client]} has left the chatroom")
                client.close()
                self.client_connected.pop(client)
                break
            # print(f"{nickname}: {message}")
            await self.broadcast_message(client, message)

    async def accept_connections(self):

        loop = asyncio.get_event_loop()

        while True:

            # client_connected, ip_address = self.server.accept()
            client_connected, ip_address = await loop.sock_accept(self.server)
            print(f"Connected to client: {ip_address}")

            # client_connected.send("You are connected successfully".encode('utf-8'))
            await loop.sock_sendall(client_connected, "You are connected successfully".encode('utf-8'))

            # nick_name = client_connected.recv(1024).decode('utf-8')
            nick_name = (await loop.sock_recv(client_connected, 1024)).decode('utf-8')
            print(f"{nick_name} has joined the chat")

            self.client_connected[client_connected] = nick_name

            task = loop.create_task(self.handle_client(client_connected, nick_name))


async def main():
    server = Server('localhost', 9090)
    await server.start_server()
    await server.accept_connections()


asyncio.run(main())


