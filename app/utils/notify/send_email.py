from typing import List
from app.utils.notify.providers import AbstractNotificationProvider


class EmailNotification:
    provider = None

    def __init__(self, provider: AbstractNotificationProvider):
        self.provider = provider()

    def send(self, to_emails: List[str], subject: str, html_content: str):
        return self.provider.send_email(to_emails=to_emails, subject=subject, html_content=html_content)

