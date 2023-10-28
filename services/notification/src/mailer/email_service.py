import asyncio
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import os
from jinja2 import Environment, FileSystemLoader
from config import settings
import aiosmtplib


templates_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'templates'))
env = Environment(loader=FileSystemLoader(templates_dir))

logger = logging.getLogger(__name__)


async def send_account_created_email(to_email, username):
    subject = "Account Created"
    template = env.get_template("account_created_email.html")
    body = template.render(username=username, email=to_email)

    msg = MIMEMultipart()
    msg["From"] = settings.MAIL_DEFAULT_SENDER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    smtp = aiosmtplib.SMTP(hostname=settings.SMTP_SERVER,
                           port=settings.SMTP_PORT,
                           use_tls=True)
    try:
        await smtp.connect()
        await smtp.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        await smtp.send_message(msg)

    except aiosmtplib.SMTPException as e:
        logger.error('SMTP Exception: {}'.format(e))
    finally:
        await smtp.quit()
