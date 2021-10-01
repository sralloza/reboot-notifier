from typing import Generator, List

from pydantic import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    admin_id: int
    other_ids: List[int] = []

    @property
    def chat_ids(self) -> Generator[int, None, None]:
        yield self.admin_id
        yield from self.other_ids


settings = Settings()
