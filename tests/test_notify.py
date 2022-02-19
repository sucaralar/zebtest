from app.utils.notify import Notify


def send_mail(app):
    subject = "unit test"
    emails = ["sucaralar@gmail.com", "sucarrilloa@gmail.com"]
    content = "This is an awesome email from zebtest demo"

    notify = Notify(subject=subject, emails=emails, content=content)
    notify.send()

