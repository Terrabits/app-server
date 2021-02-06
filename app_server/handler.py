import asyncio
import aiohttp
from   aiohttp import web


def get(address, port):
    async def handler(request):
        # open websocket
        websocket = web.WebSocketResponse()
        await websocket.prepare(request)

        # open instrument connection
        instr_reader, instr_writer = \
            await asyncio.open_connection(address, port)

        async def incoming_handler():
            async for msg in websocket:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    instr_writer.write(msg.data.strip().encode() + b'\n')
                    await instr_writer.drain()
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    exception = websocket.exception
                    print(f'websocket closed: {exception}', flush=True)

        async def outgoing_handler():
            while True:
                data = await instr_reader.read(64_000)
                await websocket.send_str(data.decode())

        await asyncio.gather(incoming_handler(), outgoing_handler())
        return websocket
    return handler
