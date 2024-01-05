from contextlib import asynccontextmanager

from aiogram import Bot
from aiogram import Dispatcher
from starlette.requests import Request

from .fastapi_extended import FastAPIExtended
from src.bot import setup_bot
from src.bot import setup_dispatcher
from src.config import Config
from src.config import load_config
from src.constants import CONFIG_FILE_PATH
from src.logger import logger


def get_application() -> FastAPIExtended:
    config: Config = load_config(filepath=CONFIG_FILE_PATH)

    @asynccontextmanager
    async def lifespan(_application: FastAPIExtended):
        _application.dp = await setup_dispatcher(config=config)
        _application.bot = await setup_bot(config=config)

        await logger.awarning(f"Starting bot with {config}")
        await logger.ainfo("Graceful startup")

        yield

        await _application.bot.session.close()
        await logger.ainfo("Graceful shutdown")

    application = FastAPIExtended(
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
        debug=False,
        config=config,
        lifespan=lifespan,
    )

    @application.post(config.bot.webhook_path)
    async def bot_webhook(request: Request, update: dict):
        _app: FastAPIExtended = request.app
        _bot: Bot = _app.bot
        _dp: Dispatcher = _app.dp
        await _dp.feed_raw_update(bot=_bot, update=update)

    return application


app = get_application()

__all__ = ["app"]
