from aiohttp import web

def Logs(request):
    """Logs"""
    content = open("log.txt", "r").read()
    content = content.replace("\n", "<br>")
    new=f"""
    <h1 style='text-align: center;'>Logs<h1>
    <p style='background-color: black;border: 3px solid red; color: white;font-size: 15px'> {content} </p>"""
    return web.Response(content_type="text/html", text=new)
