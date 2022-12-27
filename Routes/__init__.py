import asyncio
from aiortc.contrib.media import MediaRelay
from .plugin import Index, Offer,Logs
# from .utils.cors import setup_cors
from aiohttp import web

app = web.Application()

relay = MediaRelay()
pcs = set()





async def on_shutdown(app):
    # close peer connections
    coros = [pc.close() for pc in pcs]
    await asyncio.gather(*coros)
    pcs.clear()

app.on_shutdown.append(on_shutdown)

app.router.add_get("/", Index)
app.router.add_post("/offer", Offer)
app.router.add_get("/logs", Logs)
# setup_cors()

