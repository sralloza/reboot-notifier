"""Configuration module."""

from typing import Generator, List

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Project settings."""

    bot_token: str
    admin_id: int
    other_ids: List[int] = []

    @property
    def chat_ids(self) -> Generator[int, None, None]:
        """Returns the list of user ids the notification must be sent to."""
        yield self.admin_id
        yield from self.other_ids


settings = Settings()
