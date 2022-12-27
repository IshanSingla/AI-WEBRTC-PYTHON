
from aiohttp import web
import os

Root = os.path.dirname(os.path.abspath(__file__))

async def Index(request):
    content = open( Root+"/index.html", "r").read()
    return web.Response(content_type="text/html", text=content)
