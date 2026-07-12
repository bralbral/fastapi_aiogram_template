from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher
from starlette.requests import Request

from src.bot import setup_bot, setup_dispatcher
from src.config import Config, load_config
from src.constants import CONFIG_FILE_PATH
from src.logger import logger

from .fastapi_extended import FastAPIExtended


def get_application() -> FastAPIExtended:
    config: Config = load_config(filepath=CONFIG_FILE_PATH)

    @asynccontextmanager
    async def lifespan(_application: FastAPIExtended):
        _application.dp = await setup_dispatcher(config=config)
        _application.bot = await setup_bot(config=config)

        await logger.ainfo("Starting bot", webhook_path=config.bot.webhook_path)
        await logger.ainfo("Graceful startup")

        try:
            yield
        finally:
            await _application.dp.storage.close()
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
    async def bot_webhook(request: Request, update: dict) -> None:
        _app: FastAPIExtended = request.app
        _bot: Bot = _app.bot
        _dp: Dispatcher = _app.dp
        await _dp.feed_raw_update(bot=_bot, update=update)

    return application


app = get_application()

__all__ = ["app"]
