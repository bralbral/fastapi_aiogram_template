from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer

from src.config import Config


async def setup_bot(config: Config) -> Bot:
    api_server = TelegramAPIServer.from_base(
        config.bot.telegram_bot_api_url, is_local=True
    )

    bot: Bot = Bot(
        token=config.bot.token.get_secret_value(),
        session=AiohttpSession(api=api_server),
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(f"{config.bot.webhook_url}")

    return bot


__all__ = ["setup_bot"]
