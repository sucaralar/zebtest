import os
import boto3
from typing import List, Any
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Content
from flask import current_app


class Notify:
    source_email = "no-reply@zdemo.mx"
    emails: List
    subject: str
    html_content: str

    def __init__(self, emails: List[str], subject: str, html_content: str):
        self.emails = emails
        self.subject = subject
        self.html_content = html_content

    def by_ses(self):
        ses_client = boto3.client('ses')
        if not self.ses_client:
            return False

        mail_template = {
            "TemplateName": 'SES_EMAIL',
            "SubjectPart": self.subject,
            "TextPart": self.content
        }

        response = ses_client.send_templated_email(
            Source=self.source_email,
            Destination={
                "ToAddresses": self.emails,
            },
            Template=mail_template
        )
        return response

    def by_sendgrid(self):

        message = Mail(
            from_email='sucaralar@gmail.com',
            to_emails=['sucaralar@gmail.com'],
            subject=self.subject,
            html_content=self.html_content)

        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

        return response

    def send(self) -> Any:
        sendgrid = self.by_sendgrid()
        # if sendgrid:
        #     return sendgrid
        # ses_response = self.by_ses()
        ses_response = True
        return ses_response









