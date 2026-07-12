from urllib.parse import urlparse

from pydantic import BaseModel, Field, SecretStr, field_validator


class BotConfig(BaseModel):
    token: SecretStr
    telegram_bot_api_url: str
    webhook_url: str
    webhook_listen_host: str = "0.0.0.0"
    webhook_listen_port: int = Field(default=9999, ge=1, le=65535)
    webhook_workers: int = Field(default=1, ge=1, le=1)
    drop_pending_updates: bool = False

    @field_validator("webhook_url")
    @classmethod
    def validate_webhook_url(cls, value: str) -> str:
        parsed = urlparse(value)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise ValueError("webhook_url must be an absolute HTTP(S) URL")
        if not parsed.path or parsed.path == "/":
            raise ValueError("webhook_url must include a non-root path")
        return value

    @property
    def webhook_path(self) -> str:
        return urlparse(self.webhook_url).path


class Config(BaseModel):
    bot: BotConfig


__all__ = ["BotConfig", "Config"]
