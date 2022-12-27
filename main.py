import logging
from aiohttp import web
from Routes import app

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="log.txt"
)

LOGGER = logging.getLogger(__name__)

LOGGER.info("Server started")


web.run_app(
    app, access_log=logging.getLogger("WEB"), host="0.0.0.0", port=8080
)
