import logging

import uvicorn

from src.app import app


def configure_webserver() -> uvicorn.Server:
    """
        Конфигурация вебухука
    :return:
    """
    server = uvicorn.Server(
        uvicorn.Config(
            app,
            host=app.config.bot.webhook_listen_host,
            port=app.config.bot.webhook_listen_port,
            workers=app.config.bot.webhook_workers,
            reload=False,
            server_header=False,
            date_header=False,
            log_level=logging.ERROR,
            loop="auto",
        ),
    )
    return server


__all__ = ["configure_webserver"]
