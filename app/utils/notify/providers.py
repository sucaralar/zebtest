import os
import abc
import boto3
from botocore.exceptions import ClientError
from typing import List
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class AbstractNotificationProvider(abc.ABC):

    @abc.abstractmethod
    def send_email(self, to_emails: List[str], subject: str, html_content: str) -> bool:
        raise NotImplementedError


class SendGridNotification(AbstractNotificationProvider):

    def send_email(self, to_emails: List[str], subject: str, html_content: str) -> bool:
        message = Mail(
            from_email=os.environ.get('EMAIL_SOURCE'),
            to_emails=to_emails,
            subject=subject,
            html_content=html_content)

        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        email_response = sg.send(message)
        if email_response.status_code == 201:
            response = True
        else:
            response = False
        return response


class AWSNotification(AbstractNotificationProvider):

    def send_email(self, to_emails: List[str], subject: str, html_content: str) -> bool:
        ses_client = boto3.client('ses')
        if not self.ses_client:
            return False

        mail_template = {
            "TemplateName": 'SES_EMAIL',
            "SubjectPart": subject,
            "HtmlPart": html_content
        }
        try:
            ses_client.send_templated_email(
                Source=os.environ.get('EMAIL_SOURCE'),
                Destination={
                    "ToAddresses": to_emails,
                },
                Template=mail_template
            )
        except ClientError as e:
            return False
        else:
            return True
