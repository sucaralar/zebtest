from app.utils.notify.send_email import EmailNotification
from app.utils.notify.providers import SendGridNotification


def test_send_mail(app):
    """ mail sending unit test """
    subject = "Zebrans unit test by Susy"
    emails = ["sucaralar@gmail.com", "sucarrilloa@gmail.com"]
    content = "This is an awesome email from zebtest demo"
    notify = EmailNotification(provider=SendGridNotification)
    send = notify.send(subject=subject,
                       to_emails=emails,
                       html_content=content)
    assert isinstance(send, bool)
    assert True == send


