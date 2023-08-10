import asyncio

from websockets.server import serve


async def lagrange_server(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(lagrange_server, "0.0.0.0", 5005):
        await asyncio.Future()

asyncio.run(main())
