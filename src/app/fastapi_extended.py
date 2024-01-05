from typing import Any

from aiogram import Bot
from aiogram import Dispatcher
from fastapi import FastAPI

from src.config import Config


class FastAPIExtended(FastAPI):
    bot: Bot
    dp: Dispatcher

    def __init__(
        self,
        config: Config,
        **extra: Any,
    ):
        super().__init__(**extra)
        self.config = config


__all__ = ["FastAPIExtended"]
