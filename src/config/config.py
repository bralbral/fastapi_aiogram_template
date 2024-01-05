from typing import Optional
from urllib.parse import urlparse

from pydantic import BaseModel
from pydantic import SecretStr


class BotConfig(BaseModel):
    token: SecretStr
    telegram_bot_api_url: str
    webhook_url: str
    webhook_workers: int

    @property
    def webhook_path(self) -> str:
        return urlparse(self.webhook_url).path

    @property
    def webhook_port(self) -> Optional[int]:
        return urlparse(self.webhook_url).port

    @property
    def webhook_host(self) -> Optional[str]:
        return urlparse(self.webhook_url).hostname


class Config(BaseModel):
    bot: BotConfig


__all__ = ["BotConfig", "Config"]
