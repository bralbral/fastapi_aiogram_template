from aiogram import Dispatcher

from .miscellaneous import misc_router


def register_handlers(dp: Dispatcher) -> Dispatcher:
    dp.include_router(misc_router)

    return dp


__all__ = ["register_handlers"]
