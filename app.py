#!/usr/bin/env python

import asyncio

from websockets.asyncio.server import serve


async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message, flush=True)


async def main():
    print("Starting", flush=True)
    async with serve(handler, "", 8001):
        await asyncio.get_running_loop().create_future()  # run forever
    print("Done", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
