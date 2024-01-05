from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.memory import SimpleEventIsolation

from src.bot.handlers import register_handlers
from src.config import Config


async def setup_dispatcher(config: Config) -> Dispatcher:
    dp: Dispatcher = Dispatcher(
        storage=MemoryStorage(),
        config=config,
        events_isolation=SimpleEventIsolation(),
    )

    register_handlers(dp)

    return dp


__all__ = ["setup_dispatcher"]
