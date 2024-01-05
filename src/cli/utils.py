import logging
import platform
from typing import Literal

import uvicorn

from src.app import app


def configure_webserver() -> uvicorn.Server:
    """
        Конфигурация вебухука
    :return:
    """
    # Speedup if uvloip is installed
    loop: Literal["auto", "uvloop"]
    if platform == "linux":
        try:
            import uvloop

            uvloop.install()
            loop = "uvloop"
        except ModuleNotFoundError:
            loop = "auto"
    else:
        loop = "auto"
    # ===============================

    server = uvicorn.Server(
        uvicorn.Config(
            app,
            host=app.config.bot.webhook_host,
            port=app.config.bot.webhook_port,
            workers=app.config.bot.webhook_workers,
            reload=False,
            forwarded_allow_ips="*",
            proxy_headers=True,
            server_header=False,
            date_header=False,
            log_level=logging.ERROR,
            loop=loop,
        ),
    )
    return server


__all__ = ["configure_webserver"]
