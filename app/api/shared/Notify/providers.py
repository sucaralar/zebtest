import os
import abc
from typing import List
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class AbstractNotificationProvider(abc.ABC):
    to_emails: List[str]
    subject: str
    html_content: str

    def __init__(self, to_emails: List[str], subject: str, html_content: str):
        self.to_emails = to_emails
        self.subject = subject
        self.html_content = html_content

    @abc.abstractmethod
    def send(self) -> bool:
        raise NotImplementedError


class SendGridNotification(AbstractNotificationProvider):

    def send(self) -> bool:
        message = Mail(
            from_email='sucaralar@gmail.com',
            to_emails=['sucaralar@gmail.com'],
            subject=self.subject,
            html_content=self.html_content)

        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        email_response = sg.send(message)
        if email_response.status_code == 201:
            response = True
        else:
            response = False
        return response

