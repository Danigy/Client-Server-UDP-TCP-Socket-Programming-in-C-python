import socket
import argparse
import asyncio
import aioconsole


class Client:

    def __init__(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

    async def connect_to_server(self, hostname, port):

        loop = asyncio.get_event_loop()

        print("Connecting client to the server")
        try:
            await loop.sock_connect(self.client, (hostname, port))
            # self.client.connect((hostname, port))
        except Exception as e:
            print(f"Error occurred while connecting client to the server: {e}")
            return

        print("Successfully connected to the server")

    async def receive_message(self):

        loop = asyncio.get_event_loop()
        # message = self.client.recv(1024).decode('utf-8')
        while True:
            message = (await loop.sock_recv(self.client, 1024)).decode('utf-8')
            if message:
                print(message)

    async def send_message(self, message):

        loop = asyncio.get_event_loop()
        try:
            # self.client.send(message.encode('utf-8'))
            await loop.sock_sendall(self.client, message.encode('utf-8'))
        except Exception as e:
            print(f"Exception occurred while sending message: {e}")
            return

        print("Message sent successfully")

    async def join_chat(self):
        loop = asyncio.get_event_loop()

        while True:
            # self.client.send(input("").encode('utf-8'))
            await loop.sock_sendall(self.client, (await aioconsole.ainput("")).encode('utf-8'))


async def main():
    parser = argparse.ArgumentParser(description="Add client variables")
    parser.add_argument('nickname', type=str)

    args = parser.parse_args()
    loop = asyncio.get_event_loop()

    client = Client()
    await client.connect_to_server('localhost', 9090)
    await client.send_message(args.nickname)

    task_1 = loop.create_task(client.join_chat())
    task_2 = loop.create_task(client.receive_message())
    await task_1
    await task_2


asyncio.run(main())
