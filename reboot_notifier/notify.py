import sys

from tenacity import retry
from tenacity.stop import stop_after_attempt
from tenacity.wait import wait_fixed

from .config import settings
from .networking import session


def retry_callback(retry_state):
    print("RETRY ERROR:", retry_state, file=sys.stderr)
    sys.exit(1)


@retry(
    stop=stop_after_attempt(10), wait=wait_fixed(10), retry_error_callback=retry_callback
)
def notify_text(msg: str):
    raise ValueError
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
