"""Main module."""

from .notify import notify_text


def main():
    """Main entrypoint."""
    notify_text("*Alert:* server rebooted")
