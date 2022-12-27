# import aiohttp_cors
# from Routes import app
# cors = aiohttp_cors.setup(app)

# def setup_cors(routs=app.router.routes()):
#     for route in list(routs):
#         cors.add(route, {
#             "*": aiohttp_cors.ResourceOptions(
#                 allow_credentials=True,
#                 expose_headers="*",
#                 allow_headers="*",
#                 allow_methods="*"
#             )
#         })
