import os
import sendgrid
import boto3
from typing import List, Any
from sendgrid.helpers.mail import Email, Mail, Content


class Notify:
    source_email = "no-reply@zdemo.mx"
    emails: List
    subject: str
    content: str

    def __init__(self, emails: List[str], subject: str, content: str):
        self.emails = emails
        self.subject = subject
        self.content = content

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
        sg_client = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email(self.source_email)
        mail = Mail(from_email,
                    to_emails=self.emails,
                    subject=self.subject,
                    plain_text_content=Content("text/plain", self.content))
        response = sg_client.client.mail.send.post(request_body=mail.get())
        return response

    def send(self) -> Any:
        sendgrid = self.by_sendgrid()
        if sendgrid:
            return sendgrid
        ses_response = self.by_ses()
        return ses_response









