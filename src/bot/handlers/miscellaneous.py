from aiogram import Bot
from aiogram import Router
from aiogram import types
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state

misc_router = Router(name="misc")


@misc_router.message(
    StateFilter(default_state),
)
async def echo_handler(message: types.Message, bot: Bot, **kwargs) -> None:
    chat_id = message.chat.id
    message_id = message.message_id

    await bot.copy_message(
        chat_id=chat_id,
        from_chat_id=chat_id,
        message_id=message_id,
        reply_to_message_id=message_id,
    )


__all__ = ["misc_router"]
