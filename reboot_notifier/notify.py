from .config import settings
from .networking import session


def notify_text(msg: str):
    for chat_id in settings.chat_ids:
        response = session.post(
            f"https://api.telegram.org/bot{settings.bot_token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": msg,
                "parse_mode": "markdown",
                "disable_web_page_preview": True,
            },
        )
        response.raise_for_status()